import math

# Entrada
numero = int(input('Digite um número: '))

# Processamento
# centena = math.trunc(numero / 100)
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10

somatorio = centena + dezena + unidade

# Saída
print(f'> O somatório dos dígitos de {numero} é {somatorio}')