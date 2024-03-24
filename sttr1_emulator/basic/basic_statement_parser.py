from typing import Optional, Callable, List

from sttr1_emulator.basic.basic_expression import NumericLiteral, SimpleVariable
from sttr1_emulator.basic.basic_expression_parser import is_valid_name_of_simple_variable, \
    try_to_parse_numeric_expression
from sttr1_emulator.basic.basic_statement import REM, GOTO, GOSUB, RETURN, PRINT, VARIABLE_ASSIGNMENT, BASICStatement


class InvalidProgramStatement(Exception):
    def __init__(self, line_nr: int, line_source: str):
        super().__init__()
        self.line_nr: int = line_nr
        self.line_source: str = line_source

    def __str__(self):
        return f'{super().__str__()}{self.line_nr} {self.line_source}'


def try_to_parse_REM(_: int, source: str) -> Optional[REM]:
    if not source.startswith(REM.keyword):
        return None
    return REM(source.removeprefix(REM.keyword))


def try_to_parse_GOTO(line_nr: int, source: str) -> Optional[GOTO]:
    if not source.startswith(GOTO.keyword):
        return None
    target_line_nr = source.removeprefix(GOTO.keyword)
    if not target_line_nr.isnumeric():
        raise InvalidProgramStatement(line_nr, source)
    return GOTO(source, int(target_line_nr))


def try_to_parse_GOSUB(line_nr: int, source: str) -> Optional[GOSUB]:
    if not source.startswith(GOSUB.keyword):
        return None
    target_line_nr = source.removeprefix(GOSUB.keyword).strip()
    if not target_line_nr.isnumeric():
        raise InvalidProgramStatement(line_nr, source)
    return GOSUB(source, int(target_line_nr))


def try_to_parse_RETURN(line_nr: int, source: str) -> Optional[RETURN]:
    if not source.startswith(RETURN.keyword):
        return None
    rest = source.removeprefix(RETURN.keyword).strip()
    if len(rest) > 0:
        raise InvalidProgramStatement(line_nr, source)
    return RETURN(source)


def try_to_parse_PRINT(_: int, source: str) -> Optional[PRINT]:
    if not source.startswith(PRINT.keyword):
        return None
    rest = source.removeprefix(PRINT.keyword).strip()

    # PRINT "                          STAR TREK "
    # PRINT "DO YOU WANT INSTRUCTIONS (THEY'RE LONG!)";
    # PRINT "YOU MUST DESTROY"K9;" KLINGONS IN"T9;" STARDATES WITH"B9;" STARBASES"
    # PRINT
    # PRINT "YOU HAVE"E" UNITS OF ENERGY"
    # PRINT  USING 5370;S1,S2
    # PRINT  USING 2520
    # PRINT  USING 2510;N[1],N[2],N[3]
    # PRINT "ENERGY AVAILABLE ="E+S"   NUMBER OF UNITS TO SHIELDS:";
    # PRINT  USING 3700;K[I,1],K[I,2]
    # PRINT "YOUR EFFICIENCY RATING ="((K7/(T-T0))*1000)
    # PRINT "YOUR ACTUAL TIME OF MISSION ="INT((((T1-T7)*.4)-T7)*100)" MINUTES"
    # PRINT  USING 4560;Q$[25,27],Q$[28,30],Q$[31,33],Q$[34,36],Q$[37,39],Q$[40,42],Q$[43,45],Q$[46,48],T
    # PRINT  USING 4570;Q$[49,51],Q$[52,54],Q$[55,57],Q$[58,60],Q$[61,63],Q$[64,66],Q$[67,69],Q$[70,72],C$
    # PRINT "\012   STATUS REPORT\012"
    # PRINT "DIRECTION ="C1+(((ABS(A)-ABS(X))+ABS(A))/ABS(A))
    # PRINT D$[S8,S8+11];
    return PRINT(source)


def try_to_parse_variable_assignment(line_nr: int, source: str) -> Optional[VARIABLE_ASSIGNMENT]:
    parts = list(map(str.strip, source.strip().split('=')))

    variables = parts[:-1]
    for v in variables:
        if not is_valid_name_of_simple_variable(v):
            raise InvalidVariableNameError(line_nr=line_nr, line_source=source, var_name=v)

    expr, _ = try_to_parse_numeric_expression(parts[-1])
    if expr is None:
        raise InvalidExpressionError(line_nr, source, parts[-1])

    return VARIABLE_ASSIGNMENT(source, vars=variables, expr=expr)




class InvalidVariableNameError(Exception):
    def __init__(self, line_nr: int, line_source: str, var_name: str):
        super().__init__()
        self.line_nr: int = line_nr
        self.line_source: str = line_source
        self.var_name = var_name

    def __str__(self):
        return f'{super().__str__()}{self.line_nr} {self.line_source}'


class InvalidExpressionError(Exception):
    def __init__(self, line_nr: int, line_source: str, expression: str):
        super().__init__()
        self.line_nr: int = line_nr
        self.line_source: str = line_source
        self.expression: str = expression

    def __str__(self):
        return f'{super().__str__()}{self.line_nr} {self.line_source}'


StatementParser = Callable[[int, str], Optional[BASICStatement]]

ALL_STATEMENT_PARSERS: List[StatementParser] = [
    try_to_parse_GOTO,
    try_to_parse_GOSUB,
    try_to_parse_RETURN,
    try_to_parse_REM,

    try_to_parse_variable_assignment,
]
