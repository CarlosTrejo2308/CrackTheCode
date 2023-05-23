import unittest
from unittest.mock import patch
import random
import main

class MainTestCase(unittest.TestCase):
    @patch('main.random')
    def test_getCode(self, mock_random):
        mock_random.randint.side_effect = [1, 3, 2, 0]  # Mock the random number generation
        code = main.getCode(length=4)
        expected_code = [1, 3, 2, 0]
        self.assertEqual(code, expected_code)

    @patch('main.random')
    def test_getCode_length_greater_than_9(self, mock_random):
        with self.assertRaises(Exception) as context:
            main.getCode(length=10)
        self.assertEqual(str(context.exception), "Length cannot be greater than 9")

if __name__ == '__main__':
    unittest.main()