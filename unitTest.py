import unittest
from main import getCode

class TestGetCode(unittest.TestCase):
    def test_get_code(self):
        length = 4
        code = getCode(length)

        # Verificar que la longitud del código sea correcta
        self.assertEqual(len(code), length)

        # Verificar que el código solo contenga dígitos
        for digit in code:
            self.assertTrue(isinstance(digit, int))

        # Verificar que el código no contenga dígitos duplicados
        self.assertEqual(len(code), len(set(code)))

if __name__ == "__main__":
    unittest.main()