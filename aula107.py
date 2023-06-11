from itertools import zip_longest

#  Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
cidades = ["Salvador", "Ubatuba", "Belo Horizonte"]
estados = ["BA", "SP", "MG", "RJ"]
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


for cidade, estado in zip(cidades, estados):
    print(cidade, estado)
print()

# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]


l1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
l2 = ["BA", "SP", "MG", "RJ"]
print(list(zip(l1, l2)))
print()
print(list(zip_longest(l1, l2, fillvalue="SEM CIDADE")))
