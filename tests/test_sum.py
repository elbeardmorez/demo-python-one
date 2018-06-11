import unittest

from lib.solutions.sum import sum


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)

    def test_validate_type(self):
        with self.assertRaises(TypeError):
            sum("pandas", 3)
        with self.assertRaises(TypeError):
            sum(10, "hippos")

    def test_validate_range(self):
        with self.assertRaises(AssertionError):
            sum(1200, 3)

    def test_validate_string_parse(self):
        self.assertEqual(sum("1", "3"), 4)


if __name__ == '__main__':
    unittest.main()
