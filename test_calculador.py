from calculador import *
import unittest

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        '''Probando suma'''
        self.assertEqual(sumar(-24,24), 0)

    def test_restar(self):
        '''Probando resta'''
        self.assertEqual(restar(8,-3), 11)

    def test_multiplicar(self):
        '''Probando multiplicacion'''
        self.assertEqual(multiplicar(5,-10), -50)
    def test_dividir(self):
        '''Probando division'''
        self.assertEqual(dividir(15,3), 5)
        with self.assertRaises(AssertionError):
            dividir(15,0)
if __name__ == '__main__':
    unittest.main()
