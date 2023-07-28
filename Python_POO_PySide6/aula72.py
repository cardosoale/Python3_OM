"""Exercícios com funções

Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variável."""


def multiplica(*args):
    """
    Retorna o produto dos valores fornecidos como argumentos.

    Args:
        *args: Valores inteiros a serem multiplicados.

    Returns:
        int: O produto dos valores fornecidos.

    Example:
        >>> multiplica(2, 3, 4)
        24
        >>> multiplica(5, 10, 2, 1)
        100"""
    produto = 1
    for multiplicador in args:
        produto *= multiplicador
        # multiplicador += 1
    return produto


RESULTADO = multiplica(3, 5, 8, 9, 10)
print(RESULTADO)
print(multiplica(1, 2, 3))
