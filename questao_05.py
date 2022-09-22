import os

def ler_texto():
    dir_arq = os.getcwd() #diretorio desse arquivo python
    dir_a = dir_arq +'/questao4/a.txt' # dir + nome
    leitura_notepad_a = open(dir_a, 'r',  encoding="utf8") # le o arquivo
    linhas_a = leitura_notepad_a.read()


    dir_b = dir_a = dir_arq +'/questao4/b.txt'
    leitura_notepad_b = open(dir_b, 'r',  encoding="utf8")
    linhas_b = leitura_notepad_b.read()

    return linhas_a, linhas_b

def calcular(lista, listb):
    if len(lista) > len(listb):
        listamaior = lista
        listamenor = listb
    elif len(listb) > len(lista):
        listamaior = listb
        listamenor = lista

    lista_soma = []
    for i in range(0, len(listamaior)):
        if i >= len(listamenor):
            listamaior[i] = int(listamaior[i])
            listamaior[i] += 0
            lista_soma.append(listamaior[i])
        else:
            listamaior[i] = int(listamaior[i])
            listamenor[i] = int(listamenor[i])
            lista_soma.append(listamaior[i] + listamenor[i])
    
    return lista_soma

def main():
    conteudo_a, conteudo_b = ler_texto()
    lista_a = conteudo_a.split()
    lista_b = conteudo_b.split()
    print('Lista A:', lista_a)
    print('Lista B:', lista_b)
    lista_soma = calcular(lista_a, lista_b)
    
    for count in range (0, len(lista_soma)):
        print('Soma da linha' ,count + 1, ':' ,lista_soma[count])

if __name__ == '__main__':
    main()