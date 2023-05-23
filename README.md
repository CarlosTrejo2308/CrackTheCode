import unittest
from your_module import getCode

class CodeGenerationTest(unittest.TestCase):
    def test_getCode(self):
        length = 4
        code = getCode(length)

        # Verificar que la longitud del código generado sea igual a la longitud esperada
        self.assertEqual(len(code), length)

        # Verificar que los elementos del código estén dentro del rango válido
        for num in code:
            self.assertGreaterEqual(num, 0)
            self.assertLessEqual(num, 9)

        # Verificar que no haya números repetidos en el código
        self.assertEqual(len(code), len(set(code)))

if __name__ == "__main__":
    unittest.main()
