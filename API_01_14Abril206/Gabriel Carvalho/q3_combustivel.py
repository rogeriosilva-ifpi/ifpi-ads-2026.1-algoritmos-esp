def main():

        consumo_estrada = 12  
        consumo_cidade = 8    

        distancia = float(input("Digite a distância total da viagem (km): "))
        while distancia <= 0:
            print("Valor inválido! Digite uma distância maior que 0.")
            distancia = float(input("Digite a distância total da viagem (km): "))

        percentual_estrada = float(input("Digite o percentual em estrada (0 a 100): "))
        while percentual_estrada < 0 or percentual_estrada > 100:
            print("Valor inválido! Digite um valor entre 0 e 100.")
            percentual_estrada = float(input("Digite o percentual em estrada (0 a 100): "))

        preco = float(input("Digite o preço do litro do combustível (R$): "))
        while preco <= 0:
            print("Valor inválido! Digite um valor maior que 0.")
            preco = float(input("Digite o preço do litro do combustível (R$): "))

        dist_estrada = distancia * (percentual_estrada / 100)
        dist_cidade = distancia - dist_estrada
        litros_estrada = dist_estrada / consumo_estrada
        litros_cidade = dist_cidade / consumo_cidade
        total_litros = litros_estrada + litros_cidade
        custo_total = total_litros * preco

        print("\n--- Resultado da Viagem ---")
        print(f"Distância em estrada: {dist_estrada:.2f} km")
        print(f"Distância na cidade: {dist_cidade:.2f} km")
        print(f"Consumo em estrada: {litros_estrada:.2f} litros")
        print(f"Consumo na cidade: {litros_cidade:.2f} litros")
        print(f"Total de litros necessários: {total_litros:.2f} litros")
        print(f"Custo total da viagem: R$ {custo_total:.2f}")


main()   
        