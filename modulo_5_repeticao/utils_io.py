def obter_inteiro(texto):
  while True:
    try:
      numero = int(input(texto))
      return numero
    except:
      print('Valor inválido!')


def obter_inteiro_minimo(texto, minimo):
  numero = obter_inteiro(texto)

  while numero < minimo:
    print(f'Valor deve ser no mínimo = {minimo}')
    numero = obter_inteiro(texto)
  
  return numero


def obter_inteiro_positivo(texto):
  return obter_inteiro_minimo(texto, 1)
