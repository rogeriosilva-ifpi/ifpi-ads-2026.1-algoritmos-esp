# definição de uma nova função
def somar(v1, v2):
  somatorio = v1 + v2
  return somatorio

r = somar(int(input('valor 1:')), int(input('valor 2:')))
r2 = somar(44, 44)

print(f'Resultado: {r}')
print(f'Resultado: {r2}')