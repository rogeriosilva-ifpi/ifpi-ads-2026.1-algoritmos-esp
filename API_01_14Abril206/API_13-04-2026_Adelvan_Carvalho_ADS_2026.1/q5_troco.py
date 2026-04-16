from utils import obter_float

def calcular_troco(valor_total, valor_pago):
    # --- PROCESSAMENTO ---
    troco = round(valor_pago - valor_total, 2)
    # Lista de cédulas e moedas disponíveis conforme o enunciado 
    cedulas_moedas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    
    # --- SAÍDA ---
    print(f"\nTroco Total: R$ {troco:.2f}")
    for valor in cedulas_moedas:
        quantidade = int(troco // valor)
        if quantidade > 0:
            tipo = "Cédula(s)" if valor >= 2 else "Moeda(s)"
            print(f"{quantidade} {tipo} de R$ {valor:.2f}")
            # Atualiza o troco restante com arredondamento para precisão
            troco = round(troco % valor, 2)

def main():
    # --- ENTRADA ---
    total_compra = 0
    while True:
        # Menu para lançar os produtos apenas pelo preço 
        preco = obter_float("Preço do produto (0 para finalizar): ")
        if preco == 0: 
            break
        total_compra += preco
        
    # --- PROCESSAMENTO / ENTRADA ---
    print(f"Total a pagar: R$ {total_compra:.2f}")
    valor_pago = obter_float("Valor pago: R$ ")
    
    # --- SAÍDA / PROCESSAMENTO ---
    # Valida se o valor pago é suficiente 
    if valor_pago >= total_compra:
        calcular_troco(total_compra, valor_pago)
    else:
        print("Erro: Valor pago é insuficiente!")

if __name__ == "__main__":
    main()