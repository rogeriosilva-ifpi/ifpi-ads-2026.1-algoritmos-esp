
from utils_io import obter_inteiro, obter_inteiro_minimo, obter_inteiro_positivo


def main():
  n = obter_inteiro_positivo('N: ')
  inferior = obter_inteiro('Inferior: ')
  superior = obter_inteiro_minimo('Superior: ', inferior + 1)

  for i in range(inferior, superior + 1):
    if i % n == 0:
      print(i, end=' ')

  print('\nFim.')


main()