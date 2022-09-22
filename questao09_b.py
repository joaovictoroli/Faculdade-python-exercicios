import random
import threading
import time

# usando thread, é alocado a execução do programa em diferentes threads dentro do processador
# dessa forma comparando os testes 3 e 4, que por mais que um teste execute mais funções que o outro
# eles são semelhantes em tempo de execução, uma vez que, a função mais demorada (t4) determina o tempo de execução.
def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)

def gerar_vetorA(tamanho):
  vetor_A = []
  for i in range (0 ,tamanho):
    inteiro_positivo = random.randrange(1,10)
    vetor_A.append(inteiro_positivo)
  
  return vetor_A

def gerar_vetorB(vector):
  vetor_B = []
  for element in vector:
    resultado = fatorial(element)
    vetor_B.append(resultado)

  return vetor_B

def main(i, tamanho):
  vetor_A = gerar_vetorA(tamanho)
  vetor_B = gerar_vetorB(vetor_A)
  print('Thread', i, 'realizada.')
  #print('Vetor A, inteiros positivos: ',vetor_A)
  #print('Vetor B, com os fatorias: ',vetor_B)

t1 = threading.Thread(target=main, args=(1, 2500))
t2 = threading.Thread(target=main, args=(2, 5000))
t3 = threading.Thread(target=main, args=(3, 10000))
t4 = threading.Thread(target=main, args=(4, 1000000))

if __name__ == '__main__':
    teste = input('Digite qual teste deseja executar: ')
    # 1- t1
    # 2- t1,t2,t3 
    # 3- t4
    # 4 - t1,t2,t3,t4
    if teste == '1':
      t_inicio = float(time.time())
      t1.start()
      t1.join()
      t_fim = float(time.time())
      print('Tempo total gasto na execução do programa: ', round(t_fim - t_inicio, 4), 'segundos')
    elif teste == '2':
      t_inicio = float(time.time())
      t1.start()
      t2.start()
      t3.start()
      t1.join()
      t2.join()
      t3.join()
      t_fim = float(time.time())
      print('Tempo total gasto na execução do programa: ', round(t_fim - t_inicio, 4), 'segundos')
    elif teste == '3':
      t_inicio = float(time.time())
      t4.start()
      t4.join()
      t_fim = float(time.time())
      print('Tempo total gasto na execução do programa: ', round(t_fim - t_inicio, 4), 'segundos')
    elif teste == '4':
      t_inicio = float(time.time())
      t1.start()
      t2.start()
      t3.start()
      t4.start()
      t1.join()
      t2.join()
      t3.join()
      t4.join()
      t_fim = float(time.time())
      print('Tempo total gasto na execução do programa: ', round(t_fim - t_inicio, 4), 'segundos')
    else:
      print('Digite um numero entre 1 a 4.')
