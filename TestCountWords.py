import unittest

from CountWords import countWords

class TestTrabajo2(unittest.TestCase):

    def test_1(self):
        frase = "hola hola como estas"
        self.assertEqual(countWords(frase), {"hola": 2, "como": 1, "estas": 1})

    def test_2(self):
        frase = "Como hola como Como si estas"
        self.assertEqual(countWords(frase), {"hola": 1, "como": 3, "estas": 1, "si": 1})

    def test_3(self):
        frase = "Como como Como como como"
        self.assertEqual(countWords(frase), {"como": 5})

    def test_4(self):
        frase = "habia un dia que Un Perro le Ladro a otro otro perro el Perro ladro"
        self.assertEqual(countWords(frase), {"habia": 1, "un": 2, "dia": 1, "que": 1, "perro": 3, "le": 1, "ladro": 2, "a": 1, "otro": 2, "el": 1})

if __name__ == "__main__":
    unittest.main()