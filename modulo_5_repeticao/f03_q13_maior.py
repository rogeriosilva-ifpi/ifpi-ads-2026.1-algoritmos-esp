def main():
  n = int(input('Quantos elementos: '))
  maior = None

  for i in range(n):
    numero = int(input('Digite um número: '))

    if not maior or numero > maior:
      maior = numero
  

  print(f'O maior número digitado é {maior}')


main()