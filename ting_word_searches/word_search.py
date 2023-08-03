def exists_word(word, instance):
    objeto = []

    for arquivo in instance._data:
        data = {
            "palavra": word,
            "arquivo": arquivo["nome_do_arquivo"],
            "ocorrencias": [],
        }
        linhas = arquivo.get("linhas_do_arquivo")
        for i, ln in enumerate(linhas):
            if word.lower() in ln.lower():
                data["ocorrencias"].append({"linha": i+1})
        if data["ocorrencias"]:
            objeto.append(data)

    return objeto


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
