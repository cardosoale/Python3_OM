"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra = 'SOROCABA'
letra_corretas = ''
contador = 0

while True:
    letra_sugerida = input('Para sair digite "0" a qualquer momento. \nDigite uma letra tentar descobrir a palavra secreta: ').upper()
    if letra_sugerida == '0':
        break

    contador += 1

    if len(letra_sugerida) != 1:
        print('Digite apenas uma letra')
            
    if letra_sugerida in palavra:
        letra_corretas += letra_sugerida

    palavra_formada = ''
    for letra in palavra:
        if letra in letra_corretas:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra:
        os.system('clear')
        print(f'Parabéns vc acertou a palavra secreta! Em {contador} tentativas.')        
        letra_corretas = ''
        contador = 0



