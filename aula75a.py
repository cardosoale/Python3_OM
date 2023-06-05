def multiplicador(mult):
    def multiplica(num):
        return num * mult
    return multiplica

# Solicitar a entrada do usuário para num e mult
num = float(input("Digite um número: "))
mult = float(input("Digite o multiplicador: "))

# Criar as funções com base nos valores fornecidos pelo usuário
# resultado = multiplicador(mult)

# Imprimir o resultado da multiplicação
print(multiplicador(mult)(num))