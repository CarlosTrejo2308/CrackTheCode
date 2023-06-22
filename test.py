import unittest
from main import getCode, compareCode

class TestGuessingGame(unittest.TestCase):
    def test_getCode(self):
        self.assertEqual(len(getCode()), 4)
        self.assertRaises(Exception, getCode, 10)

    def test_compareCode(self):
        self.assertEqual(compareCode([1, 2, 3, 4], [1, 2, 3, 4]), True)
        self.assertEqual(compareCode([1, 2, 3, 4], [4, 3, 2, 1]), False)

if __name__ == '__main__':
    unittest.main()
