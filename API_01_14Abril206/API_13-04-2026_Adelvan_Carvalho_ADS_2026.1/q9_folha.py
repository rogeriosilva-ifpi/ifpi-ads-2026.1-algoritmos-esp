from utils import obter_texto, obter_float, obter_inteiro_positivo

def calcular_salario_liquido(bruto, h_extras):
    # --- PROCESSAMENTO ---
    # 1. Hora extra vale 150% da hora normal (bruto / 220h)
    valor_hora_comum = bruto / 220
    valor_total_extra = h_extras * (valor_hora_comum * 1.5)
    
    # 2. Desconto de INSS: 11% sobre o bruto
    desconto_inss = bruto * 0.11
    
    # 3. Desconto de Vale Refeição: R$ 150,00 se bruto > R$ 2.000,00
    desconto_vr = 150.00 if bruto > 2000.00 else 0.0
    
    # 4. Cálculo final do líquido
    liquido = bruto + valor_total_extra - desconto_inss - desconto_vr
    
    return valor_total_extra, desconto_inss, desconto_vr, liquido

def main():
    try:
        # --- ENTRADA ---
        n_funcionarios = obter_inteiro_positivo("Quantidade de funcionários: ")
        
        folha_total_paga = 0
        maior_salario = -1
        menor_salario = float('inf')

        for i in range(n_funcionarios):
            print(f"\nDados do Funcionário {i+1}:")
            nome = obter_texto("Nome: ")
            bruto = obter_float("Salário Bruto (R$): ")
            horas_extras = obter_float("Quantidade de horas extras: ")
            
            # --- PROCESSAMENTO ---
            v_ext, inss, vr, liq = calcular_salario_liquido(bruto, horas_extras)
            
            # Acumula total da folha e verifica extremos
            folha_total_paga += liq
            if liq > maior_salario: maior_salario = liq
            if liq < menor_salario: menor_salario = liq
            
            # --- SAÍDA INDIVIDUAL ---
            print(f"\nEXTRATO: {nome.upper()}")
            print(f"{'Salário Bruto:':<20} R$ {bruto:>10.2f}")
            print(f"{'Horas Extras:':<20} R$ {v_ext:>10.2f} ({horas_extras:.0f}h)")
            print(f"{'INSS:':<20} R$ {inss:>10.2f}")
            print(f"{'Vale Refeição:':<20} R$ {vr:>10.2f}")
            print("-" * 35)
            print(f"{'Salário Líquido:':<20} R$ {liq:>10.2f}")

        # --- SAÍDA FINAL ---
        print("\n" + "="*35)
        print("RESUMO DA FOLHA DE PAGAMENTO")
        print(f"Maior Salário Líquido: R$ {maior_salario:.2f}")
        print(f"Menor Salário Líquido: R$ {menor_salario:.2f}")
        print(f"Total Gasto com Folha: R$ {folha_total_paga:.2f}")
        print("="*35)

    except Exception as e:
        print(f"Erro inesperado no processamento: {e}")

if __name__ == "__main__":
    main()