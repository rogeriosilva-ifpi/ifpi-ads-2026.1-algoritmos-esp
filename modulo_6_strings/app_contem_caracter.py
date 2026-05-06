def main():
  texto = input('Texto: ')
  caractere = input('Caractere: ')

  if contem_caractere(texto, caractere):
    print('Sim. Contém.')
  else:
    print('Não. Não tem.')


# in
def contem_caractere(texto, caractere):
  for c in texto:
    if c == caractere:
      return True
  
  return False

main()