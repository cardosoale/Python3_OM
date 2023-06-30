# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime

from dateutil.relativedelta import relativedelta

valor_emprestimo = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
data_fim = data_emprestimo + relativedelta(years=5)
valor_parcela = valor_emprestimo / (data_fim.year - data_emprestimo.year)
prazo = relativedelta(data_fim, data_emprestimo).years * 12
data_parcelas = []
data_parcela = data_emprestimo

while data_parcela < data_fim:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R${valor_parcela:.2f}')
