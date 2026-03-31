from utils_io import obter_inteiro


def main():
  num1 = obter_inteiro('A: ')
  num2 = obter_inteiro('B: ')

  resultado = mmc(num1, num2)

  print(f'O MMC({num1}, {num2}) == {resultado}')


def mmc(a, b):
  candidato = b

  while candidato % a != 0:
    candidato += b
  
  return candidato


main()