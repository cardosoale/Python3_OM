def listar(tarefas):
    print()
    if not tarefas:
        print("Nenhuma tarefa para listar")
        return

    print("Tarefas: ")
    for tarefa in tarefas:
        print(f"\t{tarefa}")


def desfazer(tarefas):
    print()
    if not tarefas:
        print("Nenhuma tarefa para desfazer")
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)


def refazer(tarefas):
    print()
    if not tarefas:
        print("Nenhuma tarefa para refazer")
        return

    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)


while True:
    print("Comando: listar, desfazer e refazer")
    tarefa = input("Digite uma tarefa ou comando: ")

    tarefas = []
    tarefas_refazer = []

    if tarefa == "0":
        break

    if tarefa == "listar":
        listar(tarefas)
        continue
    elif tarefa == "desfazer":
        ...
        continue
    elif tarefa == "refazer":
        ...
        continue
    else:
        ...
        continue
