from pathlib import Path

from sttr1_emulator.basic.basic_program_parser import parse_program
from sttr1_emulator.basic.basic_program import BASICProgram


def run_program_file(file: Path) -> BASICProgram:
    return run_program_text(file.read_text())


def run_program_text(text: str) -> BASICProgram:
    program: BASICProgram = parse_program(text)
    program()
    return program

