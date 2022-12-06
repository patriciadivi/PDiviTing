def exists_word(word, instance):
    resultExpect = list()
    resultOccurrences = list()

    for pos, element in enumerate(instance._data[0]["linhas_do_arquivo"]):
        if word.lower() in element.lower():
            resultOccurrences.append({"linha": pos + 1})

    if 0 < len(resultOccurrences):
        resultExpect.append({
            "palavra": word,
            "arquivo": instance._data[0]["nome_do_arquivo"],
            "ocorrencias": resultOccurrences
        })

    return resultExpect


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
