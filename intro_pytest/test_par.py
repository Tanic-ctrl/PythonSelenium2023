def es_par(num_a: int, num_b: int) -> bool:
    if num_a % 2 == 0 and num_b % 2 == 0:
        return True
    else:
        return False

def test_positive():
    result = es_par(6, 2)
    assert result, "la funcion es par debe regresar verdadero para 4 y 2"

def test_negativo():
    result = es_par(4, 3)
    assert not result, "3 no es par"
