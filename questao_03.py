import subprocess, sys
import os
from pathlib import Path

dir_arq = os.getcwd()
lista_arq = []
path_to_file = dir_arq+'/questao3/' # dir + nome

def gerar_tamanho_pasta(dir):
    tamanho = 0
    for arq in os.scandir(dir):
        tamanho += arq.stat().st_size

    return tamanho
        
def fazer_scan_dir(dir):
    for arq in os.scandir(dir):
        # checa se o arquivo é uma pasta, para calcular seu tamanho
        check_dir = dir +'/'+ arq.name
        if Path(check_dir).is_dir():
            info = {}
            info['nome'] = '/'+ arq.name
            tamanho = gerar_tamanho_pasta(check_dir)
            info['size'] = tamanho
            lista_arq.append(info)
        elif arq.is_file:
            info = {}
            info['nome'] = arq.name
            info['size'] = arq.stat().st_size
            lista_arq.append(info)

def gerar_exibição(list, dir):
    print('Informações dos arquivos no diretorio: '+ dir)
    with open(path_to_file+'questão3.txt', 'w') as f:
        f.write('Informações dos arquivos no diretorio:'+ str(dir)+'\n')

    print(path_to_file+'questão3.txt')
    for element in list:
        texto = 'Nome: ' + element['nome'] + ' - Tamanho: ' + str(element['size']) + ' bytes'
        print(texto)
        with open(path_to_file+'questão3.txt', 'a') as f:
            f.write(texto+'\n')

def key_to_sort(list):
    return list['size']

def main():
    dir = input('Digite o diretorio: ')
    print(dir)
    if dir == '':
        print('usando diretorio padrão')
        dir = dir_arq
    if not Path(dir).is_dir():
        print('O digitado não é diretorio.')
        sys.exit()
    fazer_scan_dir(dir)
    lista_arq.sort(key=key_to_sort, reverse=True)
    gerar_exibição(lista_arq, dir)

if __name__ == '__main__':
    main()


