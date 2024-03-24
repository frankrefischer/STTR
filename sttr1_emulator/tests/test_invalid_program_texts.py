import unittest
from typing import List

from sttr1_emulator.basic.basic_program_parser import parse_program, MissingLineNumberError


class TestMissingLineNumber(unittest.TestCase):
    def test_missing_line_number(self):
        program_texts = ["""
        REM
        """, """
        10 REM
        REM
        """, ]
        for i, t in enumerate(program_texts, start=1):
            with self.subTest(i_of_n=f'{i} of {len(program_texts)}'):
                with self.assertRaises(expected_exception=MissingLineNumberError):
                    parse_program(t)


def make_many_program_texts(*texts: List[str]) -> List[str]:
    return [
        make_text(*lines)
        for lines in texts
    ]


def make_text(*lines: str) -> str:
    print(type)
    return '\n'.join(lines)


if __name__ == '__main__':
    unittest.main()
