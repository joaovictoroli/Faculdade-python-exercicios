import subprocess
import os


dir_arq = os.getcwd()
notepad = "notepad.exe"

def main():
    nome_arq_txt = input('Digite o nome do arquivo de texto: ')
    dir = dir_arq +'/'+nome_arq_txt+'.txt'
    print(dir)
    subprocess.Popen([notepad, dir])

if __name__ == '__main__':
    main()