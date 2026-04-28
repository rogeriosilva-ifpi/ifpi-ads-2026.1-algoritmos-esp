def ler_produto(mensagem):
    valor = input(mensagem)
    return valor

def ler_preco(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Digite o preço válido")
        except ValueError:
            print("Valor inválido")

def ler_sistema(mensagem):
    while True:
        valor = input(mensagem).upper()
        if valor in ("S","N"):
            return valor
        else:
            print("Digite (S/N)")

def ler_valor_pago(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Forneça uma quantia")
        except ValueError:
            print("Digite um valor válido")

valor_total = 0

sistema = "S"

while sistema == "S":

    produto = ler_produto("Digite o nome do produto: ")
    preco = ler_preco(f'Digite o preço do(a) {produto}: R$ ')

    valor_total += preco

    sistema = ler_sistema("Deseja continuar lendo as notas (S/N): ")

valor_pago = ler_valor_pago("Digite o valor pago pelo cliente: ")

if valor_pago > valor_total:

    troco = valor_pago - valor_total

    troco_em_centavos = troco * 100

    nota_cem = troco_em_centavos // 10000
    resto_cem = troco_em_centavos % 10000

    nota_ciquenta = resto_cem // 5000
    resto_ciquenta = resto_cem % 5000

    nota_vinte = resto_ciquenta // 2000
    resto_vinte = resto_ciquenta % 2000

    nota_dez = resto_vinte // 1000
    resto_dez = resto_vinte % 1000

    nota_cinco = resto_dez // 500
    resto_cinco = resto_dez % 500

    nota_dois = resto_cinco // 200
    resto_dois = resto_cinco % 200

    nota_um = resto_dois // 100
    resto_um = resto_dois % 100

    ciquenta_centavos = resto_um // 50
    resto_ciquenta_centavos = resto_um % 50

    vinte_e_cinco_centavos = resto_ciquenta_centavos // 25
    resto_vinte_e_cinco_centavos = resto_ciquenta_centavos % 25

    dez_centavos = resto_vinte_e_cinco_centavos // 10
    resto_dez_centavos = resto_vinte_e_cinco_centavos % 10

    cinco_centavos = resto_dez_centavos // 5
    resto_cinco_centavos = resto_dez_centavos % 5

    um_centavo = resto_cinco_centavos // 1
    
    print("_________________STATUS PAGAMENTO_______________\n")
    print(f'Valor total: R$ {valor_total:.2f}')
    print(f'Valor pago: R$ {valor_pago:.2f}')
    print(f'Troco: R$ {troco:.2f}\n')

    print(f'Total de nota de R$ 100: {nota_cem:.0f} ')
    print(f'Total de nota de R$ 50: {nota_ciquenta:.0f} ')
    print(f'Total de nota de R$ 20: {nota_vinte:.0f} ')
    print(f'Total de nota de R$ 10: {nota_dez:.0f} ')
    print(f'Total de nota de R$ 5:  {nota_cinco:.0f}')
    print(f'Total de nota de R$ 2: {nota_dois:.0f} ')
    print(f'Total de nota de R$ 1: {nota_um:.0f}')
    print(f'Total de nota de R$ 0,50: {ciquenta_centavos:.0f}')
    print(f'Total de nota de R$ 0,25: {vinte_e_cinco_centavos:.0f} ')
    print(f'Total de nota de R$ 0,10: {dez_centavos:.0f} ')
    print(f'Total de nota de R$ 0,05: {cinco_centavos:.0f} ')
    print(f'Total de nota de R$ 0,01:  {um_centavo:.0f}')

else:
    print("Pagamento sem troco")

