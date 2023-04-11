import unittest

def contar_palabras(palabra):
    palabras = {}

    

class TestContarPalabras(unittest.TestCase):
    def test_hola(self):
        resultado = contar_palabras ("hola")
        self.assertEqual(resultado, {"hola" : 1})

    def test_2(self):
        resultado = contar_palabras("Que onda gente")
        self.assertEqual(resultado, {"Que onda gente": 2})

    def test_3(self):
        resultado = contar_palabras("Si, tenés razon")
        self.assertEqual(resultado, {"Si, tenés razon": 3})

    def test_4(self):
        resultado = contar_palabras("Hoy es un dia nefasto")
        self.assertEqual(resultado, {"Hoy es un dia nefasto": 4})

    def test_5(self):
        resultado = contar_palabras("Basicamente se cae")
        self.assertEqual(resultado, {"Basicamente se cae": 5})

    def test_6(self):
        resultado = contar_palabras("Tartaglia corrió")
        self.assertEqual(resultado, {"Tartaglia corrió": 6})

    def test_7(self):
        resultado = contar_palabras("Nombre: Bobel, Apellido: Rufino Feliz ")
        self.assertEqual(resultado, {"Nombre: Bobel, Apellido: Rufino Feliz": 7})