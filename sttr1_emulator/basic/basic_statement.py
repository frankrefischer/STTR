from dataclasses import dataclass
from typing import ClassVar, List

from sttr1_emulator.basic.basic_expression import NumericExpression
from sttr1_emulator.basic.basic_program_environment import Environment


@dataclass
class BASICStatement:
    source: str

    def __call__(self, env: Environment):
        ...


@dataclass
class REM(BASICStatement):
    keyword: ClassVar[str] = 'REM'

    def __call__(self, env: Environment):
        ...

    def __str__(self):
        return f'REM {self.source}'


@dataclass
class GOTO(BASICStatement):
    keyword: ClassVar[str] = 'GOTO'

    line_nr: int

    def __call__(self, _: Environment):
        ...

    def __str__(self):
        return f'{self.keyword} {self.line_nr}'


@dataclass
class GOSUB(BASICStatement):
    keyword: ClassVar[str] = 'GOSUB'

    line_nr: int

    def __call__(self, _: Environment):
        ...

    def __str__(self):
        return f'{self.keyword} {self.line_nr}'


@dataclass
class RETURN(BASICStatement):
    keyword: ClassVar[str] = 'RETURN'

    def __call__(self, _: Environment):
        ...

    def __str__(self):
        return f'{self.keyword}'


@dataclass
class PRINT(BASICStatement):
    keyword: ClassVar[str] = 'PRINT'

    def __call__(self, _: Environment):
        ...

    def __str__(self):
        return f'{self.keyword}'


@dataclass
class VARIABLE_ASSIGNMENT(BASICStatement):
    vars: List[str]
    expr: NumericExpression

    def __call__(self, env: Environment):
        value = self.expr.evaluate(env)
        for var in self.vars:
            var: str
            env[var] = value

    def __str__(self):
        lhs = '='.join(self.vars)
        return f'{lhs}={self.expr}'
