def main():
    consumo_por_litro_estrada = 12
    consumo_por_litro_cidade = 8

    distancia = validar_entrada('Digite a distancia (KM): ')
    percentual_em_estrada = validar_percentual('Digite o percentual da estrada: (0-100%) ')
    preco_por_litro = validar_entrada('Digite o preço do litro do combustível (R$): ')

    distancia_total_em_estrada = distancia * (percentual_em_estrada / 100)
    distancia_total_em_cidade = distancia - distancia_total_em_estrada

    consumo_total_estrada = distancia_total_em_estrada / consumo_por_litro_estrada
    consumo_total_cidade = distancia_total_em_cidade / consumo_por_litro_cidade
    consumo_total = consumo_total_cidade + consumo_total_estrada

    custo_total_viagem = preco_por_litro * consumo_total

    print(f'Distancia percorrida em estrada: {distancia_total_em_estrada} Km.')
    print(f'Distania percorrida em cidade: {distancia_total_em_cidade} Km.')
    print(f'Consumo total de combustível na estrada: {consumo_total_estrada} litros.')
    print(f'Consumo total de combustível na cidade: {consumo_total_cidade} litros.')
    print(f'Consumo total de combustível: {consumo_total}')
    print(f'Custo total da viagem: {custo_total_viagem} R$')

def validar_entrada(mensagem):
    try:
        numero = float(input(mensagem))
        if numero > 0:
            return numero
        else:
            print('Entrada inválida. Digite um número positivo.')
            return validar_entrada(mensagem)
    
    except ValueError:
        print('Entrada inválida. Digite um número')
        return validar_entrada(mensagem)
    
def validar_percentual(mensagem):
    try:
        numero = float(input(mensagem))
        if numero >= 0 and numero <= 100:
            return numero
        else:
            print('Entrada inválida. Digite um número positivo.')
            return validar_entrada(mensagem)
        
    except ValueError:
        print('Entrada inválida. Digite um número')
        return validar_entrada(mensagem)

main()