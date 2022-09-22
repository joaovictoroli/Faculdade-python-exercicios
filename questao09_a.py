import random
import time

def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)

def gerar_vetorA(tamanho):
  vetor_A = []
  for i in range (0 ,tamanho):
    inteiro_positivo = random.randrange(1,50)
    vetor_A.append(inteiro_positivo)
  
  return vetor_A

def gerar_vetorB(vector):
  vetor_B = []
  for element in vector:
    resultado = fatorial(element)
    vetor_B.append(resultado)

  return vetor_B

def main(tamanho):
  vetor_A = gerar_vetorA(tamanho)
  vetor_B = gerar_vetorB(vetor_A)
  #print('Vetor A, inteiros positivos: ',vetor_A)
  #print('Vetor B, com os fatorias: ',vetor_B)


if __name__ == '__main__':
    t_inicio = float(time.time())
    main(1000000)
    t_fim = float(time.time())
    print('Tempo total gasto na execução do programa: ', t_fim - t_inicio, 'segundos')