from utils import obter_float, obter_inteiro_positivo, obter_confirmacao

def gerar_pa(a, r, n):
    soma = 0
    print("Termos: ", end="")
    for i in range(n):
        termo = a + i * r
        print(f"{termo:.1f}", end=" ")
        soma += termo
    print(f"\nSoma: {soma:.1f} | Média: {soma/n:.1f}")

def main():
    continuar = True
    while continuar:
        a = obter_float("Primeiro termo (a): ")
        r = obter_float("Razão (r): ")
        n = obter_inteiro_positivo("Número de termos (n >= 2): ")
        if n < 2: n = 2
        
        gerar_pa(a, r, n)
        continuar = obter_confirmacao("Deseja calcular outra progressão (S/N)? ")

if __name__ == "__main__":
    main()