import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "Buen Dia")

if __name__ == '__main__':
    unittest.main()