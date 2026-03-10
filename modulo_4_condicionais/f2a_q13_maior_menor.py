def main():
  num1 = int(input('Número 1: '))
  num2 = int(input('Número 2: '))
  num3 = int(input('Número 3: '))
  num4 = int(input('Número 4: '))
  num5 = int(input('Número 5: '))

  maior = maximo(num1, num2, num3, num4, num5)
  menor = minimo(num1, num2, num3, num4, num5)

  print(f'O MAIOR valor é {maior}')
  print(f'O MENOR valor é {menor}')


def maximo(num1, num2, num3, num4, num5):
  if eh_maior_de_todos(num1, num2, num3, num4, num5):
    return num1
  elif eh_maior_de_todos(num2, num1, num3, num4, num5):
    return num2
  elif eh_maior_de_todos(num3, num1, num2, num4, num5):
    return num3
  elif eh_maior_de_todos(num4, num2, num3, num1, num5):
    return num4
  else:
    return num5
  

def minimo(num1, num2, num3, num4, num5):
  if eh_menor_de_todos(num1, num2, num3, num4, num5):
    return num1
  elif eh_menor_de_todos(num2, num1, num3, num4, num5):
    return num2
  elif eh_menor_de_todos(num3, num1, num2, num4, num5):
    return num3
  elif eh_menor_de_todos(num4, num2, num3, num1, num5):
    return num4
  else:
    return num5
  

def eh_maior_de_todos(n1, n2, n3, n4, n5):
  return n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5
   

def eh_menor_de_todos(n1, n2, n3, n4, n5):
  return n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5


main()