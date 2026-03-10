def main():
  # TODO: Criar funcao para obter dados(limite)
  nota1 = float(input('Nota 01: '))
  nota2 = float(input('Nota 02: '))

  # Processamento
  media = (nota1 + nota2) / 2
  conceito = calcular_conceito(media)
  situacao = computar_situacao(conceito)

  # Resultado / Saída
  print('Notas do Alunos:')
  print(f'\tNota 01: {nota1:.1f}')
  print(f'\tNota 02: {nota2:.1f}')
  print(f'Média: {media:.1f}')
  print(f'Conceito: {conceito}')
  print(f'Situação: {situacao}')


def calcular_conceito(media: float):
  if media >= 9.0:
    return 'A'
  elif media >= 7.5:
    return 'B'
  elif media >= 6.0:
    return 'C'
  elif media >= 4.0:
    return 'D'
  else:
    return 'E'


def computar_situacao(conceito: str):
  if conceito == 'A' or conceito == 'B' or conceito == 'C':
    return 'APROVADO'
  else:
    return 'REPROVADO'


main()