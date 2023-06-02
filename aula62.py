"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf = input('Digite seu cpf(apenas numeros): ')
cpf_dez_dig = cpf[:10]
contador_regressivo = 11

resultado_parcial_dig_2 = 0
for digito in cpf_dez_dig:
    resultado_parcial_dig_2 += int(digito) * contador_regressivo
    contador_regressivo -= 1

digito_2 = (resultado_parcial_dig_2 * 10) % 11
digito_2 = 0 if digito_2 > 9 else digito_2

print(digito_2)