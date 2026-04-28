def ler_distancia_total(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Digite a distância do percuso")
        except ValueError:
            print("Valor inválido")

def ler_percentual_estrada(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0 and valor <= 100:
                return valor
            else:
                print("Digite uma porcentagem válida")
        except ValueError:
            print("Valor inválido")

def ler_preco_litro_combustivel(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Digite o valor do litro da gasolina")
        except ValueError:
            print("Valor inválido")

distancia_total = ler_distancia_total("Digite a distância total da viagem: ")

porcentagem_trecho_estrada = ler_percentual_estrada("Digite o percentual pecorrido na estrada: ")
porcentagem_trecho_cidade = 100 - porcentagem_trecho_estrada

preco_combustivel = ler_preco_litro_combustivel("Digite o preço do litro do combustivel R$: ")

distancia_pecorrida_na_estrada_km = distancia_total * (porcentagem_trecho_estrada / 100)
distancia_pecorrida_na_cidade_km = distancia_total * (porcentagem_trecho_cidade / 100)

consumo_de_gasolina_estrada = distancia_pecorrida_na_estrada_km / 12
consumo_de_gasolina_cidade = distancia_pecorrida_na_cidade_km / 8

valor_gasto_na_estrada = consumo_de_gasolina_estrada * preco_combustivel
valor_gasto_na_cidade = consumo_de_gasolina_cidade * preco_combustivel

total_de_litros_necessarios = consumo_de_gasolina_cidade + consumo_de_gasolina_estrada

custo_total = valor_gasto_na_estrada + valor_gasto_na_cidade

print("_______________RESULTADO_______________\n")

print(f'Consumo de gasolina na cidade: {consumo_de_gasolina_cidade:.2f} litros')
print(f'Consumo de gasolina na estrada: {consumo_de_gasolina_estrada:.2f} litros')
print(f'Total de litros necessários: {total_de_litros_necessarios:.2f} litros')
print(f'Custo da viagem: R$ {custo_total:.2f}')


