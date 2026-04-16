def main():
    total = 0
    op = 1

    while op != 0:
        valor = float(input("Digite o valor do produto: "))
        total = total + valor

        op = int(input("Digite 1 para adicionar outro produto ou 0 para finalizar: "))

    pago = float(input("Digite o valor pago: "))

    if pago < total:
        print("Valor pago insuficiente")
    else:
        troco = pago - total

        print("Total da compra:", total)
        print("Troco:", troco)

        n100 = int(troco // 100)
        troco = troco % 100

        n50 = int(troco // 50)
        troco = troco % 50

        n20 = int(troco // 20)
        troco = troco % 20

        n10 = int(troco // 10)
        troco = troco % 10

        n5 = int(troco // 5)
        troco = troco % 5

        n2 = int(troco // 2)
        troco = troco % 2

        m1 = int(troco // 1)
        troco = troco % 1

        m050 = int(troco // 0.5)
        troco = troco % 0.5

        m025 = int(troco // 0.25)
        troco = troco % 0.25

        m010 = int(troco // 0.10)
        troco = troco % 0.10

        m005 = int(troco // 0.05)
        troco = troco % 0.05

        m001 = int(round(troco / 0.01))

        print("100:", n100)
        print("50:", n50)
        print("20:", n20)
        print("10:", n10)
        print("5:", n5)
        print("2:", n2)
        print("1:", m1)
        print("0.50:", m050)
        print("0.25:", m025)
        print("0.10:", m010)
        print("0.05:", m005)
        print("0.01:", m001)


main()