from dataclasses import dataclass
from typing import Tuple, Optional, Iterable

from sttr1_emulator.basic.basic_program import BASICProgram
from sttr1_emulator.basic.basic_statement import BASICStatement
from sttr1_emulator.basic.basic_statement_parser import ALL_STATEMENT_PARSERS, InvalidProgramStatement


def parse_program(text: str) -> BASICProgram:
    program = BASICProgram()
    for line in _generate_all_non_empty_lines(text):
        line_nr, line_source = consume_line_nr(line)
        statement = _parse_line(line_nr, line_source)
        if statement is None:
            raise InvalidProgramStatement(line_nr, line_source)
        program.add(line_nr, statement)
    return program


def _generate_all_non_empty_lines(source_text: str) -> Iterable[str]:
    non_empty_lines: Iterable[str] = (
        line for line in
        map(str.strip, source_text.splitlines())
        if len(line) > 0
    )
    yield from non_empty_lines


def consume_line_nr(line: str) -> Tuple[int, str]:
    line_nr: str = ''
    i = 0
    while i < len(line) and line[i].isdigit():
        line_nr += line[i]
        i += 1
    if i == 0:
        raise MissingLineNumberError(line)
    return int(line_nr), line[i:].strip()


def _parse_line(line_nr: int, line_source: str) -> Optional[BASICStatement]:
    for parse in ALL_STATEMENT_PARSERS:
        statement = parse(line_nr, line_source)
        if statement is None:
            continue
        return statement
    return None


@dataclass
class MissingLineNumberError(Exception):
    line: str
