def main():

    total_km = float(input("Qual a distancia total percorrida em km:"))
    porcentagem = float(input("Qual a porcentagem de estrada percorria(%):"))
    preco = float(input("Qual o valor do combustivel:"))

    if total_km <= 0:
        print("Valor invalido")
    elif porcentagem < 0 or porcentagem> 100:
        print("Valor invalido")
    elif preco <= 0:
        print("Valor invalido")
    else:

        estrada = total_km * (porcentagem / 100)
        cidade = total_km - estrada

        con_estrada = estrada / 12
        con_cidade = cidade / 8

        t_litros = con_cidade + con_estrada
        custo_viagem = t_litros * preco

        print(f"Consumo na estrada:{con_estrada}")
        print(f"Consumo na cidade:{con_cidade}")
        print(f"Total de litros:{t_litros}")
        print(f"Custo total da viagem:{custo_viagem}")

main()

