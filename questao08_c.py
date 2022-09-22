import random
import multiprocessing

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
  print('Multiprocess ', i)
  #print('Vetor A, inteiros positivos: ',vetor_A)
  #print('Vetor B, com os fatorias: ',vetor_B)


p1 = multiprocessing.Process(target=main, args=(1, 2500))
p2 = multiprocessing.Process(target=main, args=(2, 2500))
p3 = multiprocessing.Process(target=main, args=(3, 5000))
p4 = multiprocessing.Process(target=main, args=(4, 10000))

if __name__ == '__main__':
  p1.start()
  p2.start()
  p3.start()
  p4.start()