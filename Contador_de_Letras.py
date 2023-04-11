import unittest

def contar_let(cadena):
    resultado = {}
    for letra in cadena:
        if letra in resultado:
            resultado[letra] += 1
        else:
            resultado[letra] = 1
    return resultado

class testContarLetras(unittest.TestCase):
    def test_ejemplo1(self):
        resultado = contar_let("que onda gente")
        self.assertEqual(resultado, {'q': 1, 'u': 1, 'e': 3, ' ': 2, 'o': 1, 'n': 2, 'd': 1, 'a': 1, 'g': 1, 't': 1})

    def test_ejemplo2(self):
        resultado = contar_let("Python es genial")
        self.assertEqual(resultado, {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, ' ': 2, 'e': 2, 's': 1, 'g': 1, 'i': 1, 'a': 1, 'l': 1})

    def test_ejemplo3(self):
        resultado = contar_let("Mississippi")
        self.assertEqual(resultado, {'M': 1, 'i': 4, 's': 4, 'p': 2})

if __name__ == '__main__':
    unittest.main()



