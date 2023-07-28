# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import json

lista_a_fazer = []
lista_refazer = []
while True:
    comandos = input(
        "Digite o que deseja fazer, listar, desfazer,\
refazer, ou digite a tarefa: "
    )
    if comandos == "0":
        break
    if comandos == "listar":
        if not lista_a_fazer:
            print("Nada para listar")
        else:
            for tarefa in lista_a_fazer:
                print(tarefa)
    elif comandos == "desfazer":
        if not lista_a_fazer:
            print("Nada para desfazer")
        else:
            lista_refazer.append(lista_a_fazer.pop())
    elif comandos == "refazer":
        if not lista_refazer:
            print("Nada para refazer")
        else:
            lista_a_fazer.append(lista_refazer.pop())
    else:
        lista_a_fazer.append(comandos)


