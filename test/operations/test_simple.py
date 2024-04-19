import unittest

from src.operations.simple import add


class MyTestCase(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add(2, 5), 7)  # add assertion here


if __name__ == '__main__':
    unittest.main()
