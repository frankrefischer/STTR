from dataclasses import dataclass, field
from typing import Dict, List, cast

from sttr1_emulator.basic.basic_statement import BASICStatement, GOTO, GOSUB, RETURN
from sttr1_emulator.basic.basic_program_environment import Environment


@dataclass
class ReturnWithoutGosubError(Exception):
    statement: BASICStatement


@dataclass
class DuplicateLineNumberError(Exception):
    line_nr: int


@dataclass
class ProgramState:
    sorted_line_numbers: List[int]
    program_counter: int = 0
    return_stack: List[int] = field(default_factory=list)
    env: Environment = field(default_factory=dict)

    def lookup_line_nr(self) -> int:
        return self.sorted_line_numbers[self.program_counter]

    def execute(self, statement: BASICStatement):
        if type(statement) is GOTO:
            goto = cast(GOTO, statement)
            self.do_goto(goto.line_nr)
        elif type(statement) is GOSUB:
            gosub = cast(GOSUB, statement)
            self.do_gosub(gosub.line_nr)
        elif type(statement) is RETURN:
            if len(self.return_stack) == 0:
                raise ReturnWithoutGosubError(statement)
            self.do_return()
        else:
            statement(self.env)
            self.program_counter += 1

    def do_goto(self, line_nr: int):
        self.program_counter = self.sorted_line_numbers.index(line_nr)

    def do_gosub(self, line_nr: int):
        self.return_stack.append(self.program_counter + 1)
        self.do_goto(line_nr)

    def do_return(self):
        caller_program_counter = self.return_stack.pop()
        self.program_counter = caller_program_counter


@dataclass
class BASICProgram:
    program: Dict[int, BASICStatement] = field(default_factory=dict)
    state: ProgramState = None

    def __len__(self):
        return len(self.program)

    def __call__(self):
        self.state = ProgramState(sorted_line_numbers=sorted(self.program.keys()))

        while 0 <= self.state.program_counter < len(self.state.sorted_line_numbers):
            statement = self.next_statement()
            self.state.execute(statement)

    def next_statement(self) -> BASICStatement:
        line_nr = self.state.lookup_line_nr()
        return self.program[line_nr]

    def add(self, line_nr: int, statement: BASICStatement):
        if line_nr in self.program:
            raise DuplicateLineNumberError(line_nr)
        self.program[line_nr] = statement
