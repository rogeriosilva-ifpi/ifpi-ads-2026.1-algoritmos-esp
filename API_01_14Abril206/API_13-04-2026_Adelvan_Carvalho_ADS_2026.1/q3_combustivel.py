from utils import obter_float, obter_float_faixa

def calcular_viagem(distancia, pct_estrada, preco_litro):
    # --- PROCESSAMENTO ---
    dist_estrada = distancia * (pct_estrada / 100)
    dist_cidade = distancia - dist_estrada
    
    litros_estrada = dist_estrada / 12
    litros_cidade = dist_cidade / 8
    
    total_litros = litros_estrada + litros_cidade
    custo_total = total_litros * preco_litro
    
    return litros_estrada, litros_cidade, total_litros, custo_total

def main():
    # --- ENTRADA ---
    distancia = obter_float("Distância total (km): ")
    pct_estrada = obter_float_faixa("Percentual em estrada (0-100): ", 0, 100)
    preco_litro = obter_float("Preço do litro (R$): ")
    
    # --- PROCESSAMENTO ---
    l_est, l_cid, total_l, custo = calcular_viagem(distancia, pct_estrada, preco_litro)
    
    # --- SAÍDA ---
    print(f"\nConsumo Estrada: {l_est:.2f} L")
    print(f"Consumo Cidade: {l_cid:.2f} L")
    print(f"Total de Litros: {total_l:.2f} L")
    print(f"Custo Total: R$ {custo:.2f}")

if __name__ == "__main__":
    main()