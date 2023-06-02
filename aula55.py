"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal
 
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}') # retorna string
print(type(f'{numero_3:.2f}')) # retorna string
print(round(numero_3, 4)) # retorna mesmo tipo(float)
print(type(round(numero_3, 4))) # retorna mesmo tipo(float) usando o método Decimal, muda o tipo