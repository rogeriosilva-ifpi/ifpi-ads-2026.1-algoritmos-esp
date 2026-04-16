from utils import obter_texto, obter_inteiro_positivo

# --- PROCESSAMENTO ---
def classificar_dimensao(escore, eh_realizacao=False):
    if not eh_realizacao:
        if escore <= 2.0: return "Baixo" [cite: 109]
        if escore <= 3.9: return "Moderado" [cite: 109]
        return "Alto" [cite: 109]
    else:
        # A lógica de classificação é inversa para Realização Pessoal 
        if escore <= 2.0: return "Alta" [cite: 109]
        if escore <= 3.9: return "Moderada!" [cite: 109]
        return "Baixa" [cite: 109]

def obter_respostas():
    # --- ENTRADA ---
    respostas = []
    for i in range(1, 10):
        while True:
            try:
                # Somente inteiros de 0 a 6 são aceitos 
                r = int(input(f"Resposta afirmação {i} (0-6): "))
                if 0 <= r <= 6:
                    respostas.append(r)
                    break
                print("Erro: Digite um valor entre 0 e 6.") [cite: 87]
            except ValueError:
                print("Erro: Entrada inválida. Digite um número inteiro.") [cite: 87]
    return respostas

def calcular_escores(respostas):
    # --- PROCESSAMENTO ---
    # Escore = média das respostas das perguntas correspondentes [cite: 107]
    exaustao = sum(respostas[0:3]) / 3 [cite: 107]
    desperso = sum(respostas[3:6]) / 3 [cite: 107]
    realizacao = sum(respostas[6:9]) / 3 [cite: 107]
    return exaustao, desperso, realizacao

def exibir_laudo(nome, ex, de, re):
    # --- SAÍDA ---
    print(f"\n==== LAUDO: {nome.upper()}") [cite: 116]
    c_ex = classificar_dimensao(ex)
    c_de = classificar_dimensao(de)
    c_re = classificar_dimensao(re, True)
    
    print(f"Exaustão Emocional : {ex:.2f} - {c_ex}") [cite: 117, 118, 119]
    print(f"Despersonalização   : {de:.2f} - {c_de}") [cite: 122]
    print(f"Realização Pessoal  : {re:.2f} - {c_re}") [cite: 123, 121]
    
    # Verificação de níveis críticos para o alerta do laudo [cite: 124]
    criticos = 0
    if c_ex == "Alto": criticos += 1
    if c_de == "Alto": criticos += 1
    if c_re == "Baixa": criticos += 1
    
    if criticos >= 2:
        print(f"Atenção: {criticos} dimensão(ões) em nível crítico.") [cite: 124]
        print("Recomenda-se acompanhamento profissional.") [cite: 124]

def main():
    try:
        # --- ENTRADA ---
        n = obter_inteiro_positivo("Quantidade de respondentes: ") [cite: 83]
        
        dados_estudo = []
        soma_respostas_burnout = 0
        total_perguntas_burnout = 0

        for _ in range(n):
            nome = obter_texto("Nome do respondente: ") [cite: 84]
            respostas = obter_respostas() [cite: 84, 86]
            
            # --- PROCESSAMENTO ---
            ex, de, re = calcular_escores(respostas) [cite: 85, 86]
            
            # Média Geral Burnout usa apenas Exaustão e Despersonalização 
            soma_respostas_burnout += sum(respostas[0:6])
            total_perguntas_burnout += 6
            
            dados_estudo.append({"nome": nome, "ex": ex, "re": re})
            
            # --- SAÍDA ---
            exibir_laudo(nome, ex, de, re) [cite: 86]

        # --- RESUMO FINAL ---
        if n > 0:
            # Identifica maior exaustão e menor realização [cite: 128, 131]
            maior_ex = max(dados_estudo, key=lambda x: x['ex']) [cite: 130]
            menor_re = min(dados_estudo, key=lambda x: x['re']) [cite: 132]
            media_geral = soma_respostas_burnout / total_perguntas_burnout [cite: 134]

            print("\n======= RESUMO DO ESTUDO =======") [cite: 126]
            print(f"Respondentes      : {n}") [cite: 127, 129]
            print(f"Maior Exaustão    : {maior_ex['nome']} ({maior_ex['ex']:.2f})") [cite: 128, 130]
            print(f"Menor Realização  : {menor_re['nome']} ({menor_re['re']:.2f})") [cite: 131, 132]
            print(f"Média Geral Burnout: {media_geral:.2f}") [cite: 133, 134]

    except Exception as e:
        print(f"Erro no processamento geral: {e}") [cite: 73]

if __name__ == "__main__":
    main()