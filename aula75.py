# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro

def multiplicador(mult):
    def multiplica(num):
        return(num * mult)
    return multiplica

dobro = multiplicador(2)
triplo = multiplicador(3)
quadruplo = multiplicador(4)

print(dobro(2))
print(triplo(2))
print(quadruplo(2))