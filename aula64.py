import re
import random

# cpf = (input('Digite o seu cpf: ')) # poderia usar .replace('-', ''), varias vezes.
# cpf = re.sub(r'[^0-9]', '', cpf)
nove_digitos = ''
for digito in range(9):
    nove_digitos += str(random.randint(0, 9))

contador_regressivo_1 = 10
res_parcial_dig_1 = 0
for digito in nove_digitos:
    res_parcial_dig_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (res_parcial_dig_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_dig = f'{nove_digitos}{digito_1}'
contador_regressivo_2 = 11

resultado_parcial_dig_2 = 0
for digito in dez_dig:
    resultado_parcial_dig_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_parcial_dig_2 * 10) % 11
digito_2 = 0 if digito_2 > 9 else digito_2

cpf_valido = nove_digitos + str(digito_1) + str(digito_2)
print(cpf_valido)
