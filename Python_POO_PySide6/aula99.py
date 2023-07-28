# from sys import path


# import aula99_package.modulo  # metodo 1
# from aula99_package.modulo import soma_do_modulo  # metodo 2
# from aula99_package import modulo  # metodo 3
import aula99_package  # metodo 4 através do __init__
# from aula99_package import soma_do_modulo

# from aula99_package.modulo import soma_do_modulo
# from aula99_package import modulo

# print(*path, sep="\n")
print(aula99_package.modulo.soma_do_modulo(1, 2))  # metodo 1
# print(soma_do_modulo(1, 2))  # metodo 2
# print(modulo.soma_do_modulo(1, 2))  # metodo 3
