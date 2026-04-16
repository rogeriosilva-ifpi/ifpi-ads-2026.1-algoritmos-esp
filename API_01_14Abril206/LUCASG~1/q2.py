

def main():
    inicio = int(input("Digite um numero inteiro: "))
    limite = int(input("Digite outro numero inteiro: "))
    soma = 0

    for divisor in range(inicio,limite,2):
        if inicio % divisor == 1 and divisor % 3 == 0:
            print(divisor)
            soma = soma + divisor
    print(f'A soma dos divisores é de {soma}')



main()