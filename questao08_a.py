import random

def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)

def gerar_vetorA():
  tamanho = random.randrange(1,10)
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

def main():
  vetor_A = gerar_vetorA()
  vetor_B = gerar_vetorB(vetor_A)
  print('Vetor A, inteiros positivos: ',vetor_A)
  print('Vetor B, com os fatorias: ',vetor_B)


if __name__ == '__main__':
  main()