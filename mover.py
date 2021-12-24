import os
import pathlib

def mover_arquivos(caminho_origem, caminho_destino, formato):
    lista = list(set(str(path.parent) for path in pathlib.Path(f"{caminho_origem}\\.").glob(f"**/*{formato}")))
    nome_arquivo = list()
    aux = 0
    for c in lista:
        nome_arquivo.append(pathlib.PureWindowsPath(str(lista[aux])).name)
        aux+=1
    aux = 0
    for arquivo in lista: 
        os.rename(f"{arquivo}", f"{caminho_destino}\\{nome_arquivo[aux]}")
        aux+=1
