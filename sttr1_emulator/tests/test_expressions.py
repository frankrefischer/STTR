import unittest
from typing import List, Dict

from sttr1_emulator.basic.basic_program_emulator import run_program_text


class TestNumericExpressions(unittest.TestCase):
    def test_valid_assignments(self):
        for lines, expected_env in [
            (["10 X=1+2"],
             {'X': 3}),
        ]:
            lines: List[str]
            expected_env: Dict[str, int]
            text = '\n'.join(lines)
            env = run_program_text(text).state.env
            with self.subTest(prog=text, expected_env=expected_env, env=env):
                self.assertEqual(expected_env, env)


if __name__ == '__main__':
    unittest.main()
