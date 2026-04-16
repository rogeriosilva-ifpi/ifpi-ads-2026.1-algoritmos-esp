def main():
    v1 = int(input("Digite um valor: "))
    v2 = int(input("Digite outro valor: "))
    intervalo(v1, v2)
   

def intervalo(v1, v2):
    while True:
        for i in range(v1 + v2):
            if i % 3:
                print(f'Os numeros pares sao {i}')



if __name__ == "__main__":
    main()