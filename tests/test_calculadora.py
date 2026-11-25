import pytest

from calculadora import (
    aplicar_desconto,
    dividir,
    multiplicar,
    somar,
    subtrair,
)


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


def test_desconto_valido():
    assert aplicar_desconto(200, 10) == pytest.approx(180)


def test_desconto_percentual_invalido():
    with pytest.raises(ValueError):
        aplicar_desconto(100, 150)

def test_desconto_preco_negativo():
    with pytest.raises(ValueError):
        aplicar_desconto(-10, 10)
