import socket
import sys
import pickle
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(os.getcwd())
msg = input("Entre com um diretorio completo: ")

try:
    s.connect((socket.gethostname(), 9999))
    s.send(msg.encode('utf-8'))
    bytes = s.recv(100000)
except Exception as erro:
    print(str(erro))
    sys.exit(1)

lista = pickle.loads(bytes)


if lista:
    print('Resposta: ')
    for element in lista:
        print('Nome:' ,element['nome'], '- Tamanho:' ,element['size'], 'bytes')

