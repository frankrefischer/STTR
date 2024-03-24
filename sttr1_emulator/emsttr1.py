from pathlib import Path

import click

from sttr1_emulator.basic.basic_program_emulator import run_program_file
from sttr1_emulator.basic.basic_program import BASICProgram
from sttr1_emulator.utils import ClickPathLibPath


@click.command()
@click.argument('SOURCEFILE',
                type=ClickPathLibPath(dir_okay=False, readable=True),
                default=Path(__file__).with_name('STTR1'))
def main(sourcefile: Path):
    program: BASICProgram = run_program_file(sourcefile)
    print(f'program has {len(program)} line statements')


if __name__ == '__main__':
    main()
