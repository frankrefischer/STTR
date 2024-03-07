from dataclasses import dataclass, field
from typing import List

from instructions import Instruction


@dataclass
class Statement:
    number: int
    instruction: Instruction

    @staticmethod
    def parse(text: str) -> 'Statement':
        number, instruction = text.split(sep=' ', maxsplit=1)
        number: str
        instruction: str

        number: int = int(number)
        instruction: Instruction = Instruction.parse(instruction)
        return Statement(number=number, instruction=instruction)


@dataclass
class HP_Basic_Program:
    statements: List[Statement] = field(default_factory=list)
