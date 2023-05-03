import pytest


class Calculadora:
   def __init__(self):
       pass

   def suma(self, num_a: int, num_b: int):
       return num_a + num_b

   def resta(self, num_a: int, num_b: int):
       return num_a - num_b

   def multiplicacion(self, num_a: int, num_b: int):
       return num_a * num_b

   def division(self, num_a: int, num_b: int):
       return num_a // num_b

#######################
# Test Cases
#######################
def test_suma_valida():
    calculator = Calculadora()
    result = calculator.suma(2,2)
    assert result == 4, "La suma de 2+2 debe ser igual a 4"

def test_resta_valida():
    calculator = Calculadora()
    result = calculator.resta(2, 2)
    assert result == 0, "La resta de 2-2 debe ser igual a 0"

def test_multiplicacion_valida():
    calculator = Calculadora()
    result = calculator.multiplicacion(4, 2)
    assert result == 8, "La multiplicacion de 4*2 debe ser igual a 8"

def test_division_valida():
    calculator = Calculadora()
    result = calculator.division(4, 2)
    assert result == 2, "La division de 4/2 debe ser igual a 2"