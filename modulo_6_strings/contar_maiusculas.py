def main():
  texto = input('Texto: ')

  qtd_maiusculas = contar_letras_maiusculas(texto)
  qtd_minusculas = contar_letras_minusculas(texto)
  qtd_espacos = contar_espacos(texto)
  qtd_numeros = contar_numeros(texto)

  resultado = f'''
  Análise do Texto (Tamanho: {len(texto)})
  > Letras Maiúsculas: {qtd_maiusculas}
  > Letras Minúsculas: {qtd_minusculas}
  > Números: {qtd_numeros}
  > Espaços: {qtd_espacos}
  '''
  print(resultado)


def contar_letras_maiusculas(texto):
  contador = 0
  for c in texto:
    if ord(c) >= 65 and ord(c) <= 90:
      contador += 1
  
  return contador


def contar_letras_minusculas(texto):
  contador = 0
  for c in texto:
    if ord(c) >= 97 and ord(c) <= 122:
      contador += 1
  
  return contador


def contar_numeros(texto):
  contador = 0
  for c in texto:
    if ord(c) >= 48 and ord(c) <= 57:
      contador += 1
  
  return contador


def contar_espacos(texto):
  contador = 0
  for c in texto:
    if c == ' ':
      contador +=1
  
  return contador


main()