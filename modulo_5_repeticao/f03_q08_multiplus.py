def main():
  n = int(input('N: '))
  superior = int(input('Superior: '))
  inferior = int(input('Inferior: '))

  for i in range(inferior, superior + 1):
    if i % n == 0:
      print(i)


main()