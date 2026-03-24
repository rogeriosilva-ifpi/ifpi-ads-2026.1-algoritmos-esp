def main():
  numero = int(input('Número: '))

  while not eh_primo(numero):
    numero = int(input('Outro número: '))
  
  print(f'O número {numero} é PRIMO!')


def eh_primo(numero):
  for c in range(2, numero//2 + 1): 
    if numero % c == 0:
      return False
  
  return True


main()