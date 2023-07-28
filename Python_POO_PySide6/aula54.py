"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista_compras = []
while True:
    

    entrada = input('Digite [s]air, [a]pagar, [i]nserir e [l]istar os itens da lista:\n').strip().lower()
          
    if entrada == 's':
        break
    elif entrada == 'i':
        os.system('clear')
        produto = input('Digite o produto que gostaria de inserir na lista de compras: ')
        lista_compras.append(produto)
    elif entrada == 'a':
        apagar_indice = input('Digite o índice do produto que gostaria de apagar da lista de compras: ')
        try:  
            indice = int(apagar_indice)
            lista_compras.pop(indice)
        except ValueError:
           print('Caractere inválido!')
           continue        
        except IndexError:
            print('Índice fora do range! Para saber o range pressione "l" para listar.')
            continue
        except Exception:
            print('Erro desconhecido')
            continue
    elif entrada == 'l':
        os.system('clear')
        if len(lista_compras) == 0:
            print('Nada para listar')
        for i, n in enumerate(lista_compras):
            print(i, n)
    else:
        print('Opção inválida!')
        
        