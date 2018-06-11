import unittest
from lib.solutions.checkout import checkout, build_state


class TestCheckout(unittest.TestCase):

    p = None

    def setUp(self):
        (self.p) = build_state()

    def test_checkout(self):
        self.assertEqual(checkout("AB"), self.p['A'] + self.p['B'])

    def test_checkout2(self):
        self.assertEqual(checkout("AAAAA"), 200)

    def test_checkout_dirty_input(self):
        self.assertEqual(checkout(" A   B "), -1)

    def test_checkout_multi(self):
        self.assertEqual(checkout("ABA"), 2*self.p['A'] + self.p['B'])

    def test_checkout_offer(self):
        self.assertEqual(checkout("AABBA"), 130 + 45)

    def test_checkout_illegal(self):
        self.assertEqual(checkout("pandas"), -1)

    def test_checkout_illegal2(self):
        self.assertEqual(checkout("Ax"), -1)

    def test_checkout_new_product(self):
        self.assertEqual(checkout("EE"), 2*self.p['E'])

    def test_checkout_bogof(self):
        self.assertEqual(checkout("BEE"), 2*self.p['E'])

    def test_checkout_bogof2(self):
        self.assertEqual(checkout("EEB"), 2*self.p['E'])

    def test_checkout_bogof_first(self):
        self.assertEqual(checkout("EEEEBB"), 4*self.p['E'])

    def test_checkout_bogof_first2(self):
        self.assertEqual(checkout("BEBEEE"), 4*self.p['E'])

    def test_checkout_bogof_first3(self):
        self.assertEqual(checkout("ABCDEABCDE"),
            2*self.p['A'] + self.p['B'] + 2*self.p['C'] + 2*self.p['D'] + 2*self.p['E'])

    def test_checkout_2f(self):
        self.assertEqual(checkout("FF"), 2*self.p['F'])

    def test_checkout_offer_2f(self):
        self.assertEqual(checkout("FFF"), 2*self.p['F'])

    def test_checkout_offers_free_p5(self):
        self.assertEqual(checkout(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            sum(x for x in p.values()))

    def test_checkout_offers_free_p5(self):
        self.assertEqual(checkout(
            "EERRRNNNBMQ"),
             80 + 120 + 150)

    def test_checkout_offers_value_p5(self):
        self.assertEqual(checkout(
            "AAAAAAAABBFFFHHHHHHHHHHHHHHHKKPPPPPQQQUUUUVVVVV"),
            200 + 130 + 45 + 20 + 80 + 45 + 120 + 200 + 80 + 120 + 130 + 90)

    def test_checkout_offers_all_p5(self):
        self.assertEqual(checkout(
            "AAAAAAAABBFFFHHHHHHHHHHHHHHHKKPPPPPQQQUUUUVVVVV" +
            "EERRRNNNBMQ"),
            (200 + 130 + 45 + 20 + 80 + 45 + 120 + 200 + 80 + 120 + 130 + 90) +
            (80 + 120 + 150))

