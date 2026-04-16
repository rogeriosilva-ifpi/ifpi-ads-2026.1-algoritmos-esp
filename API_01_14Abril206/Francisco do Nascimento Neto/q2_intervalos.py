def main():
    n = int(input("Digite N:"))
    m = int(input("Digite M:"))
    soma = 0
    verificar = 0



    for i in range(n, m + 1):
        if i % 2 != 0:
            if i % 3 == 0:
                print(i)
                soma += i
                verificar = 1
    
    if verificar == 1:
        print(f"Soma:{soma}")
    else:
        print("Nenhum numero satisfaz a condição")    

main()