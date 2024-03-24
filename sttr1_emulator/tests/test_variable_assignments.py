import unittest

from sttr1_emulator.basic.basic_program_emulator import run_program_text
from sttr1_emulator.basic.basic_statement_parser import InvalidVariableNameError, InvalidExpressionError


class TestNumericAssignments(unittest.TestCase):
    def test_valid_names(self):
        for var_name in [
            'A', 'X', 'Z',
            'A1', 'X6', 'Z9',
        ]:
            with self.subTest(var_name=var_name):
                run_program_text(f'10 {var_name}=0')

    def test_invalid_names(self):
        for var_name in [
            'x', '_', '0', 'Ä',
            'XX', '0X', '00', '__', '_0', '0_',
        ]:
            with self.subTest(var_name=var_name):
                with self.assertRaises(expected_exception=InvalidVariableNameError):
                    run_program_text(f'10 {var_name}=0')

    def test_valid_assignments(self):
        for lines, expected_env in [
            (["10 X=0"],
             {'X': 0}),
            (["10 Y=0"],
             {'Y': 0}),
            (["10 X=Y=0"],
             {'X': 0, 'Y': 0}),
            (["10 X=Y=Z=0"],
             {'X': 0, 'Y': 0, 'Z': 0}),
            (["10 X1=X2=X3=X4=X5=X6=X7=X8=X9=X0=0"],
             {'X1': 0, 'X2': 0, 'X3': 0, 'X4': 0, 'X5': 0, 'X6': 0, 'X7': 0, 'X8': 0, 'X9': 0, 'X0': 0, }),

            (["10 X=0", "20 Y=X"],
             {'X': 0, 'Y': 0}),
            (["10 Z=0", "20 Y=Z"],
             {'Y': 0, 'Z': 0}),
            (["10 Z=0", "20 X=Y=Z"],
             {'X': 0, 'Y': 0, 'Z': 0}),
        ]:
            text = '\n'.join(lines)
            env = run_program_text(text).state.env
            with self.subTest(prog=text, expected_env=expected_env, env=env):
                self.assertEqual(expected_env, env)

    def test_invalid_assignments(self):
        for text, expected_error in [
            ("10 =", InvalidVariableNameError),
            ("10 X=", InvalidExpressionError),
            ("10 0=", InvalidVariableNameError),
            ("10 =0", InvalidVariableNameError),
            ("10 =X", InvalidVariableNameError),
            ("10 0=0", InvalidVariableNameError),
            ("10 0=X", InvalidVariableNameError),

            ("10 X=Y=", InvalidExpressionError),
            ("10 X==0", InvalidVariableNameError),
            ("10 =Y=0", InvalidVariableNameError),
            ("10 X==", InvalidVariableNameError),
            ("10 =Y=", InvalidVariableNameError),
            ("10 ==0", InvalidVariableNameError),
            ("10 ==", InvalidVariableNameError),
        ]:
            with self.subTest(prog=text):
                with self.assertRaises(expected_exception=expected_error):
                    run_program_text(text)


if __name__ == '__main__':
    unittest.main()
