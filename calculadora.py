"""
Calculadora simples.
Projeto de exemplo para demonstrar um pipeline básico de
Integração Contínua (CI) com GitHub Actions.
"""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b


if __name__ == "__main__":
    print("Calculadora simples")
    print("2 + 3 =", somar(2, 3))
    print("10 - 4 =", subtrair(10, 4))
    print("6 * 7 =", multiplicar(6, 7))
    print("20 / 4 =", dividir(20, 4))
