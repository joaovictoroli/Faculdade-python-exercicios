import psutil
import os
import subprocess


def main():
    dir_arq = os.getcwd() #diretorio desse arquivo python
    dir = dir_arq +'/questao2/texto.txt' # dir + nome
    print('Diretorio: ',dir)

    leitura_notepad = open(dir, 'r',  encoding="utf8") # le o arquivo
    linhas = leitura_notepad.read()
    print('Conteudo original: ')
    print(linhas)
    print('-------------')
    print('Conteudo reverso: ')
    print(linhas[::-1])


if __name__ == '__main__':
    main()