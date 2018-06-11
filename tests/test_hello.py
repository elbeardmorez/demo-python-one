import unittest

from lib.solutions.hello import hello


class TestSum(unittest.TestCase):
    def test_hello(self):
        self.assertTrue("Hello" in hello("Bob"))
    def test_hello_no_arg(self):
        self.assertTrue("Hello" in hello())

