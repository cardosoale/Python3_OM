"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = input('Digite o seu cpf(somente numeros): ')
nove_digitos = cpf[:9]
contador_regressivo = 10


res_parcial_dig_1 = 0
for digito in nove_digitos:
    res_parcial_dig_1 += int(digito) * contador_regressivo
    contador_regressivo -= 1

resultado_dig_1 = (res_parcial_dig_1 * 10) % 11
resultado_dig_1 = resultado_dig_1 if resultado_dig_1 <= 9 else 0
print(resultado_dig_1)

