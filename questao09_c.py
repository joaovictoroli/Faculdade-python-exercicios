import random
import multiprocessing
import time

# O multiprocessing faz com que o programa atinja uma melhor performance, porque essa biblioteca roda o programa paralelamente
# com o surjimento de subprocessos. Comparando os resultados dos testes, 2 - 3 - 4, torna-se evidente sua melhora de rendimento.
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
  print('Multiprocessing', i, 'realizada.')
  #print('Vetor A, inteiros positivos: ',vetor_A)
  #print('Vetor B, com os fatorias: ',vetor_B)

p1 = multiprocessing.Process(target=main, args=(1, 2500))
p2 = multiprocessing.Process(target=main, args=(2, 5000))
p3 = multiprocessing.Process(target=main, args=(3, 10000))
p4 = multiprocessing.Process(target=main, args=(4, 1000000))

if __name__ == '__main__':
    teste = input('Digite qual teste deseja executar: ')
    # 1- t1
    # 2- t1,t2,t3 
    # 3- t4
    # 4 - t1,t2,t3,t4
    if teste == '1':
      t_inicio = float(time.time())
      p1.start()
      p1.join()
      t_fim = float(time.time())
      print('Tempo total gasto na execução do programa: ', round(t_fim - t_inicio, 4), 'segundos')
    elif teste == '2':
      t_inicio = float(time.time())
      p1.start()
      p2.start()
      p3.start()
      p1.join()
      p2.join()
      p3.join()
      t_fim = float(time.time())
      print('Tempo total gasto na execução do programa: ', round(t_fim - t_inicio, 4), 'segundos')
    elif teste == '3':
      t_inicio = float(time.time())
      p4.start()
      p4.join()
      t_fim = float(time.time())
      print('Tempo total gasto na execução do programa: ', round(t_fim - t_inicio, 4), 'segundos')
    elif teste == '4':
      t_inicio = float(time.time())
      p1.start()
      p2.start()
      p3.start()
      p4.start()
      p1.join()
      p2.join()
      p3.join()
      p4.join()
      t_fim = float(time.time())
      print('Tempo total gasto na execução do programa: ', round(t_fim - t_inicio, 4), 'segundos')
    else:
      print('Digite um numero entre 1 a 4.')
