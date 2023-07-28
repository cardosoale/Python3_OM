# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

# import json
import locale
from datetime import datetime
import string
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula183.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float | int) -> str:
    brl = locale.currency(val=numero, symbol=True, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='AC Consultoria & Negócios',
    telefone='+55 (15) 98825-6265'
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))

with CAMINHO_ARQUIVO.open('r') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))


# para mudar o delimitador de $ para outro caractere

# class MyTemplate(string.Template):
#     delimiter = '%'


# with CAMINHO_ARQUIVO.open('r') as arquivo:
#     texto = arquivo.read()
#     template = MyTemplate(texto)
#     print(template.substitute(dados))
