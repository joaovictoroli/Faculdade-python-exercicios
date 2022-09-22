import socket
from time import sleep

HOST = socket.gethostname() 
PORT = 9991 

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

print('Aguarde conexão.\n--------------')
msg = 'info_memoria'
udp.settimeout(5)
udp.sendto(msg.encode('utf-8'), dest)
while msg != 'sair': 
    (msg, servidor) = udp.recvfrom(1024)
    print('Se conectando à:',servidor)
    print('Resposta:')
    if msg.decode('utf-8'):
        print(msg.decode('utf-8'))
        break
    else:
        for i in range(1,5):
            sleep(5)
            msg = 'info_memoria'
            udp.sendto(msg.encode('utf-8'), dest)
            if msg.decode('utf-8'):
                print(msg.decode('utf-8'))
                break
        break #

udp.close()

