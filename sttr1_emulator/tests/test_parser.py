import unittest

from sttr1_emulator.basic.basic_program_parser import consume_line_nr


class Lexer(unittest.TestCase):
    def test_consume_line_nr(self):
        for line, expected in [
            ('123 xyz', (123, 'xyz')),
            ('123xyz', (123, 'xyz')),
            ('123 xyz ', (123, 'xyz')),
            ('123', (123, '')),
        ]:
            with self.subTest(line=line, expected=expected):
                self.assertEqual(expected, consume_line_nr(line))


if __name__ == '__main__':
    unittest.main()
