import re

cpf = (input('Digite o seu cpf: ')) # poderia usar .replace('-', ''), varias vezes.
cpf = re.sub(r'[^0-9]', '', cpf)
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

if len(cpf) != 11:
    print('Quantidade de dígitos não forma um CPF válido.')
elif cpf == cpf[0] * 11:
    print('Entrada inválida.')
else:
    res_parcial_dig_1 = 0
    for digito in nove_digitos:
        res_parcial_dig_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1

    digito_1 = (res_parcial_dig_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_dig = cpf[:10]
    contador_regressivo_2 = 11

    resultado_parcial_dig_2 = 0
    for digito in dez_dig:
        resultado_parcial_dig_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_parcial_dig_2 * 10) % 11
    digito_2 = 0 if digito_2 > 9 else digito_2

    cpf_valido = cpf[:9] + str(digito_1) + str(digito_2)
    if cpf == cpf_valido:
        print('CPF válido')
    else:
        print('CPF inválido')

    # print(f'O dois digitos validos para esse CPF({cpf}) são: {digito_1}{digito_2}')