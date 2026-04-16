def main():
    distancia = int(input("Digite a ditancia em KM dessa viagem: "))
    percentual = int(input("Qual a porcentagem do tanque: "))
    preco = float(input("Qual o preço da gasolina? "))
    calcular(distancia, percentual, preco)


def calcular(distancia, percentual, preco):
    consumo = distancia * preco
    valor_viagem = distancia * preco
    if distancia / consumo == distancia:
        print(f'O consumo foi de {consumo}L de gailina e a viagem custou {valor_viagem}')
    return calcular



if __name__ == "__main__":
    main()
