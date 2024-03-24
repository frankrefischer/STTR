from dataclasses import dataclass
from typing import Optional, Tuple, Union

from sttr1_emulator.basic.basic_expression import NumericExpression, SimpleVariable, NumericLiteral, PLUS, \
    MULT, MINUS, NumericOperator, NumericOperatorExpression


def try_to_parse_numeric_expression(text: str) -> Tuple[Optional[NumericExpression], str]:
    if len(text) == 0:
        return None, text
    left: Optional[NumericExpression] = None
    op: Optional[NumericOperator] = None
    right: Optional[NumericExpression] = None

    rest = text
    while right is None:
        token, rest = next_token(rest)
        if left is None:
            if not (isinstance(token, NumericLiteral) or isinstance(token, SimpleVariable)):
                return None, text
            if len(rest) == 0:
                return token, rest
            else:
                left = token
        elif op is None:
            if not isinstance(token, NumericOperator) or len(rest) == 0:
                return None, text
            op = token
        else:
            if not (isinstance(token, NumericLiteral) or isinstance(token, SimpleVariable)):
                return None, text
            right = token
    return NumericOperatorExpression(operator=op,
                                     left_operand=left,
                                     right_operand=right), rest


Token = Union[
    NumericOperator,
    SimpleVariable,
    PLUS,
    MINUS,
    MULT,
]


def next_token(text: str) -> Tuple[Token, str]:
    for parse in ALL_TOKEN_PARSERS:
        token, rest = parse(text)
        if token is not None:
            return token, rest.strip()
    raise InvalidExpressionError(text)


@dataclass
class InvalidExpressionError(Exception):
    text: str


def try_to_consume_numeric_literal(text: str) -> Tuple[Optional[NumericLiteral], str]:
    i = 0
    while i < len(text) and text[i].isnumeric():
        i += 1
    if i == 0:
        return None, text
    return NumericLiteral(value=int(text[:i])), text[i:]


def try_to_consume_simple_variable(text: str) -> Tuple[Optional[SimpleVariable], str]:
    if is_valid_name_of_simple_variable(text[:2]):
        return SimpleVariable(text[:2]), text[2:]

    if is_valid_name_of_simple_variable(text[:1]):
        return SimpleVariable(text[:1]), text[1:]

    return None, text


def is_valid_name_of_simple_variable(name: str):
    if not (1 <= len(name) <= 2):
        return False

    n0 = name[0]
    if not (n0.isascii() and n0.isupper() and n0.isalpha()):
        return False

    return len(name) == 1 or name[1].isnumeric()


def try_to_consume_numeric_operator(text: str) -> Tuple[Optional[NumericOperator], str]:
    if text[0] == '+':
        return PLUS(), text[1:]
    if text[0] == '-':
        return MINUS(), text[1:]
    if text[0] == '*':
        return MULT(), text[1:]
    return None, text


ALL_TOKEN_PARSERS = [
    try_to_consume_numeric_literal,
    try_to_consume_simple_variable,
    try_to_consume_numeric_operator,
]
