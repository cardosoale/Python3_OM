# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print("Abrindo Arquivo")
        arquivo = open(caminho_arquivo, modo, encoding="utf8")
        yield arquivo
    except Exception as e:
        print("Ocorreu o erro: ", e)
    finally:
        print("Fechando arquivo")
        arquivo.close()


with my_open("aula150.txt", "w") as arquivo:
    arquivo.write("linha 1 \n")
    arquivo.write("linha 2 \n", 123)
    arquivo.write('linha 3 \n')
    print('with', arquivo)
