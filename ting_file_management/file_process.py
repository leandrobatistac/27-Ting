from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    linhas = txt_importer(path_file)
    objeto = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(linhas),
        "linhas_do_arquivo": linhas,
    }

    for itens in instance._data:
        if itens["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(objeto)
    print(objeto, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
