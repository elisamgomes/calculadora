import pytest
from calculadora import somar, subtrair, multiplicar, dividir


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(10, 4) == 6


def test_multiplicar():
    assert multiplicar(6, 7) == 42


def test_dividir():
    assert dividir(20, 4) == 5


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)
