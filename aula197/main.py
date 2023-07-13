from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# import Pillow

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

# page0 = reader.pages[0]
# imagem0 = page0.images[0]
# print(page0.extract_text())
# print(page0.images[13])
# print(page0.extract_text())
# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)

# writer = PdfWriter()
# writer.add_page(page0)


for i, page in enumerate(reader.pages):
    writer = PdfWriter()

    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)

merger = PdfMerger()

files = [
    PASTA_NOVA / 'page0.pdf',
    PASTA_NOVA / 'page1.pdf',
]

for file in files:
    merger.append(file)

# merger.write(PASTA_NOVA / 'merged.pdf')
# merger.close()

    with open(PASTA_NOVA / 'merged_with', 'wb') as arquivo:
        merger.write(arquivo)
