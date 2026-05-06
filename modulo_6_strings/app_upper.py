def main():
  texto = input('Texto: ')

  texto_upper = upper(texto)

  print(texto_upper)


def upper(texto):
  novo_texto = ''
  
  for c in texto:
    if eh_letra_minuscula(c):
      novo_c = chr(ord(c) - 32)
      novo_texto = novo_texto + novo_c
    else:
      novo_texto = novo_texto + c
  
  return novo_texto



def eh_letra_minuscula(c):
  return ord(c) >= 97 and ord(c) <= 122

main()