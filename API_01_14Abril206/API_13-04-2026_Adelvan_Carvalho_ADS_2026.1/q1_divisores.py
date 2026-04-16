from utils import obter_inteiro_positivo

def buscar_divisores(n):
    # --- PROCESSAMENTO ---
    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(str(i))
    return divisores

def main():
    # --- ENTRADA ---
    n = obter_inteiro_positivo("Digite um número inteiro positivo: ") # [cite: 102]

    # --- PROCESSAMENTO ---
    lista_divisores = buscar_divisores(n)
    total = len(lista_divisores)

    # --- SAÍDA ---
    print("\nSaída:")
    print(f"Divisores: {' '.join(lista_divisores)}") # [cite: 106]
    print(f"Total: {total} divisores") # [cite: 107]

if __name__ == "__main__":
    main()