import unittest

from CountWords import countWords

class TestTrabajo2(unittest.TestCase):

    def test_1(self):
        resultado = countWords("hola hola como estas")
        self.assertEqual(resultado, {"hola": 2, "como": 1, "estas": 1})

    def test_2(self):
        resultado = countWords("Como hola como Como si estas")
        self.assertEqual(resultado, {"hola": 1, "como": 3, "estas": 1, "si": 1})

    def test_3(self):
        resultado = countWords("Como como Como como como")
        self.assertEqual(resultado, {"como": 5})

    def test_4(self):
        resultado = countWords("habia un dia que Un Perro le Ladro a otro otro perro el Perro ladro")
        self.assertEqual(resultado, {"habia": 1, "un": 2, "dia": 1, "que": 1, "perro": 3, "le": 1, "ladro": 2, "a": 1, "otro": 2, "el": 1})

    def test_5(self):
        resultado = countWords("hola Hola Como como Estas estas perro casa auto")
        self.assertEqual(resultado, {"hola": 2, "como": 2,"estas": 2,"perro": 1,"casa": 1,"auto": 1})
if __name__ == "__main__":
    unittest.main()