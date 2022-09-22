import subprocess
import os


dir_arq = os.getcwd()
notepad = "notepad.exe"

def main():
    dir = input('Digite o diretorio: ')
    nome_arq_txt = input('Digite o nome do arquivo de texto: ')
    if dir == '':
        dir = dir_arq +'/questao2/'+nome_arq_txt # dir + nome
    else:
        dir = dir+'/'+nome_arq_txt
    subprocess.Popen([notepad, dir])
    print(dir)

if __name__ == '__main__':
    main()