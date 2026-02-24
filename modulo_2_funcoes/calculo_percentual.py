def calcular_porcentagem(valor, percentual):
  juros = valor * (percentual/100)
  return juros


total = float(input('Valor total: '))
percentual = float(input('Qual %? '))
r = calcular_porcentagem(total, percentual)

print(f'{percentual}% de {total} é igual a {r}')