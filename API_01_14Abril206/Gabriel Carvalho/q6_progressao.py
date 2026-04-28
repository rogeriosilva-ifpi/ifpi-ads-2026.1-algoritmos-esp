def main():

    continuar = 1

    while continuar == 1:
        
        a = float(input("Digite o primeiro termo (a): "))
        r = float(input("Digite a razão (r): "))
        
        n = int(input("Digite o número de termos (mínimo 2): "))
        
        
        while n < 2:
            print("Valor inválido! Digite pelo menos 2.")
            n = int(input("Digite o número de termos (mínimo 2): "))

        print("Progressão Aritmética:")

        contador = 0
        termo = a
        soma = 0

        
        while contador < n:
            print(termo)
            soma = soma + termo
            termo = termo + r
            contador = contador + 1

       
        media = soma / n

        
        print("\nSoma dos termos:", soma)
        print("Média dos termos:", media)

        
        print("Deseja calcular outra PA?")
        print("1 - Sim")
        print("0 - Não")
        continuar = int(input("Escolha: "))

    print("Programa encerrado.")


main()