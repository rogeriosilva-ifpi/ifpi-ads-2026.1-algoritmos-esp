# Vc nunca vai ser bom no que faz pouco!

# Entrada
numero = int(input('Digite um número: '))

# Processamento
centena = numero // 100
resto = numero % 100

dezena = resto // 10
unidade = resto % 10

reverso = unidade*100 + dezena*10 + centena*1

# Saída
print(f'O número {numero} invertido fica {reverso}')