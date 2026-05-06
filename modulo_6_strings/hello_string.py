def main():
  texto = input('Digite um texto: ')

  # for item in texto:
  #   print(item)

  for i in range(len(texto)):
    print(i, texto[i], ord(texto[i]))


main()