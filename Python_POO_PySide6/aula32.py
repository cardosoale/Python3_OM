"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um numero inteiro: ')
try:
    num_int = int(num)
    if num_int % 2 == 0:
        print(f' O numero digitado "{num_int}" é par.')
    else:
        print(f' O numero digitado "{num_int}" é impar.')

except:
    print('Isso não é um caractere válido!')
    

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite apenas a hora, entre "0 e 23": ')

try:
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 23:
        if hora_int <= 11:
            print('Bom dia')
        elif hora_int <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')
    else:
            print('Vc não digitou um horario fora do especificado')

except:
    print('Vc não digitou um horario válido')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
primeiro_nome = input('Digite seu primeiro nome: ')
if len(primeiro_nome) < 3:
    primeiro_nome = input('Nome muito curto, digite seu primeiro nome: ')
elif len(primeiro_nome) < 5:
    print('Seu nome é curto')
elif len(primeiro_nome) < 7:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')