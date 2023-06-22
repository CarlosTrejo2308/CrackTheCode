import unittest
from unittest.mock import patch
from your_module import getUserAttempt

class GetUserAttemptTestCase(unittest.TestCase):
    def test_valid_input(self):
        with patch('builtins.input', return_value='1234'):
            result = getUserAttempt()
            self.assertEqual(result, [1, 2, 3, 4])

    def test_invalid_length(self):
        with patch('builtins.input', return_value='12345'), patch('builtins.print') as mock_print:
            result = getUserAttempt()
            self.assertIsNone(result)
            mock_print.assert_called_once_with("Error. Length of code should be: 4")

    def test_invalid_input(self):
        with patch('builtins.input', return_value='12a3'), patch('builtins.print') as mock_print:
            result = getUserAttempt()
            self.assertIsNone(result)
            mock_print.assert_called_once_with("Something went wrong, make sure to only use numbers!")

if __name__ == '__main__':
    unittest.main()
