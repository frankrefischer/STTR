from dataclasses import dataclass
from typing import Union

from sttr1_emulator.basic.basic_program_environment import Environment

Numeric = Union[int, float]


@dataclass
class NumericExpression:
    def evaluate(self, env: Environment) -> Numeric:
        ...

    def __str__(self):
        ...


@dataclass
class NumericLiteral(NumericExpression):
    value: Union[int, float]

    def evaluate(self, _: Environment):
        return self.value

    def __str__(self):
        return str(self.value)


@dataclass
class SimpleVariable(NumericExpression):
    var_name: str

    def evaluate(self, env: Environment) -> Numeric:
        return env[self.var_name]

    def __str__(self):
        return str(self.var_name)


class NumericOperator:
    def apply(self, left_operand: Numeric, right_operand: Numeric) -> Numeric:
        ...

    def __str__(self):
        ...


class PLUS(NumericOperator):
    def apply(self, left_operand: Numeric, right_operand: Numeric) -> Numeric:
        return left_operand + right_operand

    def __str__(self):
        return '+'


class MINUS(NumericOperator):
    def apply(self, left_operand: Numeric, right_operand: Numeric) -> Numeric:
        return left_operand - right_operand

    def __str__(self):
        return '-'


class MULT(NumericOperator):
    def apply(self, left_operand: Union[float, int], right_operand: Union[float, int]):
        return left_operand * right_operand

    def __str__(self):
        return '*'


@dataclass
class NumericOperatorExpression(NumericExpression):
    operator: NumericOperator
    left_operand: NumericExpression
    right_operand: NumericExpression

    def evaluate(self, env: Environment):
        left_value = self.left_operand.evaluate(env)
        right_value = self.right_operand.evaluate(env)
        return self.operator.apply(left_value, right_value)

    def __str__(self):
        return str(f'{self.left_operand}{self.operator}{self.right_operand}')
