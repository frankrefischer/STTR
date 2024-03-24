import unittest

from pysttr0.sttr0 import STRING, DIM_STRING


class test_STRING(unittest.TestCase):
    def test_DIM_STRING_len(self):
        for d in (0, 1, 3):
            length = len(DIM_STRING(d))
            with self.subTest(d=d, len=length):
                self.assertEqual(d, length)

    def test_DIM_STRING_capacity_mismatch(self):
        for d in (0, 1, 3):
            with self.subTest(d=d):
                with self.assertRaises(AssertionError):
                    s: STRING = DIM_STRING(d)
                    s.set((d+1)*'.')
                with self.assertRaises(AssertionError):
                    s: STRING = STRING(d * 'x')
                    s.set((d+1)*'.')

    def test_len(self):
        for s in ('', 'a', 'abc'):
            length = len(STRING(s))
            with self.subTest(s=s, expected_len=len(s), len=length):
                self.assertEqual(len(s), length)

    def test_equal(self):
        for s in ('', 'a', 'abc'):
            with self.subTest(s=s):
                self.assertTrue(s == STRING(s))
                self.assertTrue(STRING(s) == s)
                self.assertTrue(STRING(s) == STRING(s))

    def test_unequal(self):
        for s in ('', 'a', 'abc'):
            with self.subTest(s=s):
                self.assertTrue('123' != STRING(s))
                self.assertTrue(STRING('123') != s)
                self.assertTrue(STRING('123') != STRING(s))

    def test_get_slice_is_1_based(self):
        for s in ('1', 'a'):
            for start, stop in [(0,1)]:
                with self.subTest(s=s, slice=f'[{start}:{stop}]'):
                    self.assertEqual(s[0:1], STRING(s)[1:1])

    def test_get_slice(self):
        s = '12345'
        for start, stop, expected in [
            (1, 5, '12345'),
            (2, 5, '2345'),
            (4, 5, '45'),
            (5, 5, '5'),
            (1, 2, '12'),
            (1, 1, '1'),
        ]:
            with self.subTest(s=s, slice=f'[{start}:{stop}]', expected=expected):
                self.assertEqual(STRING(s)[start:stop], expected)


if __name__ == '__main__':
    unittest.main()
