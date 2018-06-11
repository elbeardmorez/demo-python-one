import unittest
from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout("AB"), 80)

    def test_checkout2(self):
        self.assertEqual(checkout("AAAAA"), 200)

    def test_checkout_dirty_input(self):
        self.assertEqual(checkout(" A   B "), -1)

    def test_checkout_multi(self):
        self.assertEqual(checkout("ABA"), 130)

    def test_checkout_offer(self):
        self.assertEqual(checkout("AABBA"), 175)

    def test_checkout_illegal(self):
        self.assertEqual(checkout("pandas"), -1)

    def test_checkout_illegal2(self):
        self.assertEqual(checkout("AX"), -1)

    def test_checkout_new_product(self):
        self.assertEqual(checkout("EE"), 80)

    def test_checkout_bogof(self):
        self.assertEqual(checkout("BEE"), 80)

    def test_checkout_bogof2(self):
        self.assertEqual(checkout("EEB"), 80)

