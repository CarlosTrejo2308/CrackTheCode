import unittest
from unittest.mock import patch
from io import StringIO
from code_breaker import getCode, getUserAttempt, compareCode

class TestCodeBreaker(unittest.TestCase):
    def test_getCode(self):
        # Prueba que el código generado tenga la longitud correcta
        length = 4
        code = getCode(length)
        self.assertEqual(len(code), length)

        length = 8
        code = getCode(length)
        self.assertEqual(len(code), length)

        length = 10
        with self.assertRaises(Exception):
            getCode(length)

    @patch('builtins.input', return_value='1234')
    def test_getUserAttempt(self, mock_input):
        # Prueba que la función getUserAttempt devuelva la entrada del usuario en forma de lista de números
        expected_result = [1, 2, 3, 4]
        result = getUserAttempt()
        self.assertEqual(result, expected_result)

    def test_compareCode(self):
        # Prueba la función compareCode para una suposición correcta e incorrecta
        guess = [1, 2, 3, 4]
        code = [1, 2, 3, 4]
        result = compareCode(guess, code)
        self.assertTrue(result)

        guess = [1, 2, 4, 3]
        code = [1, 2, 3, 4]
        result = compareCode(guess, code)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
