# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(x):
    impar_par = x % 2
    if impar_par == 0:
        return 'Par'
    return  'Ímpar'
    
resultado = par_impar(6)
print(resultado)
print(par_impar(5))
