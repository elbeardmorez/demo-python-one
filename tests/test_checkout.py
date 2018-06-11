import unittest
from lib.solutions.checkout import checkout


class TestSum(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout("AB"), 80)

    def test_checkout_dirty_input(self):
        self.assertEqual(checkout(" A   B "), -1)

    def test_checkout_multi(self):
        self.assertEqual(checkout("ABA"), 130)

    def test_checkout_offer(self):
        self.assertEqual(checkout("AABBA"), 175)

    def test_checkout_illegal(self):
        self.assertEqual(checkout("pandas"), -1)

    def test_checkout_illegal2(self):
        self.assertEqual(checkout("AE"), -1)

