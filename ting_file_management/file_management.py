import sys


def txt_importer(path_file):
    formato = '.txt'
    if formato not in path_file:
        print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file, 'r') as file:
            linhas = file.read().split('\n')
            return linhas
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
