def ler_numero(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Digite um número inteiro positivo")
        except ValueError:
            print("Valor inválido")

total_de_divisores = 0

numero = ler_numero("Digite um número inteiro positivo: ")

for i in range(1, numero + 1):

    if numero % i == 0:
        total_de_divisores += 1
        print(i)
    
print(f'Total de divisores: {total_de_divisores}')