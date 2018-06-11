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
        self.assertEqual(checkout("Ax"), -1)

    def test_checkout_new_product(self):
        self.assertEqual(checkout("EE"), 80)

    def test_checkout_bogof(self):
        self.assertEqual(checkout("BEE"), 80)

    def test_checkout_bogof2(self):
        self.assertEqual(checkout("EEB"), 80)

    def test_checkout_bogof_first(self):
        self.assertEqual(checkout("EEEEBB"), 160)

    def test_checkout_bogof_first2(self):
        self.assertEqual(checkout("BEBEEE"), 160)

    def test_checkout_bogof_first3(self):
        self.assertEqual(checkout("ABCDEABCDE"), 280)

    def test_checkout_2f(self):
        self.assertEqual(checkout("FF"), 20)

    def test_checkout_offer_2f(self):
        self.assertEqual(checkout("FFF"), 20)

    def test_checkout_offers_free_p4(self):
        self.assertEqual(checkout(
            "EERRRNNNBMQ"),
             80 + 120 + 150)

    def test_checkout_offers_value_p4(self):
        self.assertEqual(checkout(
            "AAAAAAAABBFFFHHHHHHHHHHHHHHHKKPPPPPQQQUUUUVVVVV"),
            200 + 130 + 45 + 20 + 80 + 45 + 150 + 200 + 80 + 120 + 130 + 90)

    def test_checkout_offers_all_p4(self):
        self.assertEqual(checkout(
            "AAAAAAAABBFFFHHHHHHHHHHHHHHHKKPPPPPQQQUUUUVVVVV" +
            "EERRRNNNBMQ"),
            (200 + 130 + 45 + 20 + 80 + 45 + 150 + 200 + 80 + 120 + 130 + 90) +
            (80 + 120 + 150))

