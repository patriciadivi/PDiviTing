from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for eachElement in instance._data:
        if path_file in eachElement["nome_do_arquivo"]:
            return None

    resultTxtImporters = txt_importer(path_file)
    resultFinished = {
        "nome_do_arquivo": f"{path_file}",
        "qtd_linhas": len(resultTxtImporters),
        "linhas_do_arquivo": resultTxtImporters,
    }
    
    instance.enqueue(resultFinished)
    print(resultFinished)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
