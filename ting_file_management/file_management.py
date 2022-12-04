import sys

def txt_importer(path_file):
    try:
        if path_file.endswith('.txt'):
            with open(path_file, 'r') as fileReading:
                resultData = fileReading.read().splitlines()
                return resultData
        return sys.stderr.write('Formato inválido\n')
    except:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')

# splitlines é para formatar o text após '\n', E retornar em uma LISTA
# TEXTO-SEM-splitlines()-FORMATAÇÃO = "Thank you for the music\nWelcome to the jungle"
# TEXTO-COM-splitlines()-FORMATAÇÃO = ['Thank you for the music', 'Welcome to the jungle']