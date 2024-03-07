from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, List

import click

from program import HP_Basic_Program, Statement


@click.command()
@click.argument('source', type=click.Path(readable=True, dir_okay=False))
def main(source: str):
    source_file: Path = Path(source).expanduser().absolute()
    parser = HP_Basic_Parser(source_file=source_file)
    program: HP_Basic_Program = parser.parse()


@dataclass
class HP_Basic_Parser:
    source_file: Path

    def parse(self) -> HP_Basic_Program:
        program: HP_Basic_Program = HP_Basic_Program()
        for i, line in enumerate(self._generate_program_lines(), start=1):
            assert len(line) <= 72, f'line {i} is longer than 72 characters: "{line}"'
            if len(line) == 0 or not line[0].isdigit():
                continue
            try:
                program.statements.append(Statement.parse(text=line))
            except ValueError:
                raise InvalidProgramLineError(line_number=i, line=line)

        return program

    def _generate_program_lines(self) -> Iterable[str]:
        for line in self.source_file.read_text().splitlines():
            yield line


@dataclass
class InvalidProgramLineError(Exception):
    line_number: int
    line: str

    def __post_init__(self):
        super().__init__(f'line {self.line_number} is invalid: "{self.line}"')


if __name__ == '__main__':
    main()
