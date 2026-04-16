def main():

    n = int(input("Digite um numero:"))
    soma = 0

    print("Divisores:")

    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
            soma += 1

    print(f"Total:{soma}")     

main()       


    
