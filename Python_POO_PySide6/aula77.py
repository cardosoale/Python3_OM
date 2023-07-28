# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]

qtd_acertos = 0

for pergunta in perguntas:
    print(pergunta["Pergunta"])
    print()

    opcoes = pergunta["Opções"]
    for i, opcao in enumerate(pergunta["Opções"]):
        print(f" {i}) {opcao}")
        print()

    acertou = False
    escolha = input("Escolha uma opção: ")
    qtd_opcoes = len(opcoes)

    escolha_int = None

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta["Resposta"]:
                acertou = True

    if acertou:
        print("Acertou Muleque!")
        qtd_acertos += 1
    else:
        print("Errou Caipora")

    print(f"Você acertou {qtd_acertos}/{len(perguntas)} respostas.")
