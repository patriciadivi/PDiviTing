from ting_file_management.file_management import txt_importer
import sys


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
    try:
        resultDequeue = instance.dequeue()
        if resultDequeue:
            nameDocs = resultDequeue["nome_do_arquivo"]
            print(f"Arquivo {nameDocs} removido com sucesso")
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        resultDequeue = instance.search(position)
        if resultDequeue:
            print(f"{resultDequeue}")
    except IndexError:
        print("Posição inválida", file=sys.stderr)
