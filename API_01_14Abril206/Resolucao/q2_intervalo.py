def main():
  n = int(input('N:'))
  m = int(input('N:'))
  soma = 0

  print('Divisores: ', end='')
  for numero in range(n, m+1):
    if numero % 2 != 0 and numero % 3 == 0:
      soma += numero
      print(numero, end=' ')
  
  print()
  print(f'Soma: {soma}')

main()