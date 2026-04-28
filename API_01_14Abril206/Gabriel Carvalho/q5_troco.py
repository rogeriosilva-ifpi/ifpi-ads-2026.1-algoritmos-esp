def main():

    total = 0
    opcao = 1

    
    while opcao != 0:
        print("1 - Adicionar produto")
        print("0 - Finalizar compra")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            preco = float(input("Digite o preço do produto: R$ "))
            total = total + preco

    
    print("\nTotal da compra: R$", total)

    valor_pago = 0

    while valor_pago < total:
        valor_pago = float(input("Digite o valor pago: R$ "))
        
        if valor_pago < total:
            print("Valor insuficiente! Tente novamente.")

    
    troco = valor_pago - total
    print("Troco: R$", round(troco, 2))

    
    troco_centavos = int(round(troco * 100))

    
    cedulas = [10000, 5000, 2000, 1000, 500]
    moedas = [50, 25, 10, 5, 1]

    print("Troco detalhado:")

   
    i = 0
    while i < len(cedulas):
        quantidade = troco_centavos // cedulas[i]
        if quantidade > 0:
            print(quantidade, "nota(s) de R$", cedulas[i] / 100)
            troco_centavos = troco_centavos % cedulas[i]
        i = i + 1

    
    i = 0
    while i < len(moedas):
        quantidade = troco_centavos // moedas[i]
        if quantidade > 0:
            print(quantidade, "moeda(s) de R$", moedas[i] / 100)
            troco_centavos = troco_centavos % moedas[i]
        i = i + 1


main()