from utils import obter_float, obter_float_faixa

def calcular_custo_viagem(distancia, pct_estrada, preco):
    # --- PROCESSAMENTO ---
    dist_estrada = distancia * (pct_estrada / 100)
    dist_cidade = distancia - dist_estrada
    
    litros_estrada = dist_estrada / 12 # [cite: 121]
    litros_cidade = dist_cidade / 8   # [cite: 121]
    
    total_litros = litros_estrada + litros_cidade
    custo_total = total_litros * preco
    
    return litros_estrada, litros_cidade, total_litros, custo_total

def main():
    # --- ENTRADA ---
    distancia = obter_float("Distância total (km): ") # [cite: 122]
    pct_estrada = obter_float_faixa("Percentual em estrada (0-100%): ", 0, 100) # [cite: 122]
    preco_combustivel = obter_float("Preço do litro (R$): ") # [cite: 122]

    # --- PROCESSAMENTO ---
    l_est, l_cid, t_litros, total_rs = calcular_custo_viagem(distancia, pct_estrada, preco_combustivel)

    # --- SAÍDA ---
    print(f"\nConsumo Estrada: {l_est:.2f} L") # [cite: 123]
    print(f"Consumo Cidade: {l_cid:.2f} L")    # [cite: 123]
    print(f"Total Litros: {t_litros:.2f} L")   # [cite: 123]
    print(f"Custo Total: R$ {total_rs:.2f}")   # [cite: 123]

if __name__ == "__main__":
    main()