def main():

    n = int(input("Digite um número inteiro positivo: "))

    while n <= 0:
        print("Valor inválido! Digite um número maior que 0.")
        n = int(input("Digite um número inteiro positivo: "))

    contador = 1
    quantidade = 0

    print("Divisores de", n, ":")

    while contador <= n:
        if n % contador == 0:
            print(contador)
            quantidade += 1
        contador += 1

    print("Quantidade total de divisores:", quantidade)



main()
  






   