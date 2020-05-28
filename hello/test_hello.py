import unittest
import hello


class TestHello(unittest.TestCase):
    def test_output(self):
        h = hello.Hello("Hello world")
        actual = h.output()
        self.assertEqual(actual, "Hello world")
