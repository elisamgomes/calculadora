
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


def aplicar_desconto(preco, percentual):
    if preco < 0:
        raise ValueError("Preço não pode ser negativo")
    if percentual < 0 or percentual > 100:
        raise ValueError("Percentual deve estar entre 0 e 100")
    return preco * (1 - percentual / 100)


if __name__ == "__main__":
    print("Calculadora simples")
    print("2 + 3 =", somar(2, 3))
    print("10 - 4 =", subtrair(10, 4))
    print("6 * 7 =", multiplicar(6, 7))
    print("20 / 4 =", dividir(20, 4))
