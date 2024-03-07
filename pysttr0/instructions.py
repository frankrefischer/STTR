from dataclasses import dataclass
from typing import Optional


@dataclass
class Instruction:

    @staticmethod
    def parse(text: str) -> 'Instruction':
        for instr in INSTRUCTIONS:
            instruction: Optional[Instruction] = instr.parse(text=text)
            if instruction is None:
                continue
            return instruction
        assert False, f'instruction not yet implemented: {text}'


@dataclass
class REM(Instruction):
    @staticmethod
    def parse(text:str) -> 'REM':
        ...


INSTRUCTIONS = [
    REM,
]
