def main():
    op = 1

    while op == 1:
        a = float(input("Digite o primeiro termo: "))
        r = float(input("Digite a razão: "))
        n = int(input("Digite o número de termos: "))

        if n < 2:
            print("Número inválido")
        else:
            soma = 0

            print("Sequência:")

            for i in range(n):
                termo = a + i * r
                print(termo)
                soma = soma + termo

            media = soma / n

            print("Soma:", soma)
            print("Média:", media)

        op = int(input("Deseja calcular outra? (1=sim / 0=não): "))


main()