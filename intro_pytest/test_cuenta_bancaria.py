import pytest

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No tienes suficiente saldo")
        self.saldo -= cantidad

    def consultar_saldo(self):
        print(f"saldo {self.saldo}")
        return self.saldo



class TestCuentaBancaria:

    def setup_method(self):
        self.cuenta = CuentaBancaria("Tania", 100)

    def test_one(self):
        self.cuenta.retirar(80)
        assert self.cuenta.consultar_saldo() == 20, "El saldo debe ser 20 despues de retirar 80"

    def test_two(self):
        self.cuenta.retirar(50)
        assert self.cuenta.consultar_saldo() == 50, "El saldo debe ser 50 despues de retirar 50"
