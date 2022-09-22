import subprocess
import os


notepad = "notepad.exe"

def main():
    dir_arq = input('Digite o diretorio: ')
    nome_arq_txt = input('Digite o nome do arquivo de texto: ')
    dir = dir_arq +'/'+nome_arq_txt+'.txt'
    print(dir)
    subprocess.Popen([notepad, dir])

if __name__ == '__main__':
    main()