

'''
* ler o exif dos arquivos de uma pasta
* filtrar por data
* criar uma pasta de acordo com a data dos exif
* mover arquivos para as pastas de acordo com as datas

'''
import os
def nomeArquivos ():

    nome = os.listdir()

    for f in nome:
        print(f)

nomeArquivos()

