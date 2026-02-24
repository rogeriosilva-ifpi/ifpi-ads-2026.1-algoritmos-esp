# Entrada
minutos = int(input('Minutos: '))

# Processamento
horas = minutos // 60
minutos_finais = minutos % 60

# Saída
print(f'> {minutos} minutos equivalem a {horas} horas e {minutos_finais} minutos')