# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    produto = 1
    for multiplicador in args:
        produto *= multiplicador
        # multiplicador += 1
    return produto
    
resultado = multiplica (3, 5, 8 , 9, 10)
print(resultado)
print(multiplica(1, 2, 3))