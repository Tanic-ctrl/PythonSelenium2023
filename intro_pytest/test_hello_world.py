def suma(a, b):
    return a + b


def test_hello_world():
    print("This is a test case!")
    result = suma(5, 4)
    assert result == 9, "suma de 5 + 4 debe ser 9"

def test_second_hello_world():
    print("This is a test case!")
