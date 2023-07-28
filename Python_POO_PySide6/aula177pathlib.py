from pathlib import Path
# from shutil import rmtree

caminho_projeto = Path()
# print(caminho_projeto)  # caminho relativo
# print(caminho_projeto.absolute())  # caminho absoluto

caminho_arquivo = Path(__file__)
# print()
# print(caminho_arquivo)
# print()
ideias = caminho_arquivo.parent / 'ideias'
# print(ideias / 'arquivo.txt')

# arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
# arquivo.touch()
# print(arquivo)
# arquivo. write_text('Olá Mundo')
# print(arquivo.read_text())
# arquivo.unlink()

# caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
# caminho_arquivo.touch()
# caminho_arquivo.write_text('')
# with caminho_arquivo.open('a+') as file:
#     file.write('Uma linha\n')
#     file.write('Outra linha\n')

# print(caminho_arquivo.read_text())
# caminho_arquivo.unlink()


caminho_pasta = Path.home() / 'Desktop' / 'Python is coll'

caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)
arquivo_subpasta = subpasta / 'arquivo.json'
arquivo_subpasta.touch(exist_ok=True)
arquivo_subpasta.write_text('Hey')

arquivo_pasta = caminho_pasta / 'arquivo.txt'
arquivo_pasta.touch(exist_ok=True)
arquivo_pasta.write_text("Let's Go")

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    # file.touch()

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Olá Mundo\n')
        text_file.write(f'file_{i}.txt')

# rmtree(caminho_pasta)


def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()

        else:
            print('FILE: ', file)
            file.unlink()
    if remove_root:
        root.rmdir()


rmtree(caminho_pasta)
