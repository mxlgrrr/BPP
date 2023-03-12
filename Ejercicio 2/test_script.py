import unittest
import pytest

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

class TestFunciones(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-2, 2), 0)
    
    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(0, 0), 0)
    
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)
        self.assertEqual(multiplicacion(-2, -3), 6)
    
    def test_division(self):
        self.assertEqual(division(6, 2), 3)
        self.assertRaises(ValueError, division, 6, 0)

class TestFuncionesPytest:
    
    def test_suma(self):
        assert suma(2, 3) == 5
        assert suma(-2, 2) == 0
    
    def test_resta(self):
        assert resta(5, 3) == 2
        assert resta(0, 0) == 0
    
    def test_multiplicacion(self):
        assert multiplicacion(2, 3) == 6
        assert multiplicacion(-2, -3) == 6
    
    def test_division(self):
        assert division(6, 2) == 3
        with pytest.raises(ValueError):
            division(6, 0)

if __name__ == '__main__':
    unittest.main()
