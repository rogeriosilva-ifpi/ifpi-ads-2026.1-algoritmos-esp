from utils import obter_inteiro_positivo, obter_float_faixa

def analisar_desempenho(nota):
    if nota >= 7.0:
        return "Aprovado"
    elif nota >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"

def main():
    # --- ENTRADA ---
    n_alunos = obter_inteiro_positivo("Digite a quantidade de alunos: ")
    
    soma_notas = 0
    maior_nota = 0
    menor_nota = 10
    aprovados = 0
    recuperacao = 0
    reprovados = 0

    # --- PROCESSAMENTO ---
    for i in range(n_alunos):
        nota = obter_float_faixa(f"Nota do aluno {i+1} (0-10): ", 0, 10)
        soma_notas += nota
        
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota
            
        situacao = analisar_desempenho(nota)
        print(f"Situação: {situacao}")
        
        if situacao == "Aprovado":
            aprovados += 1
        elif situacao == "Recuperação":
            recuperacao += 1
        else:
            reprovados += 1

    media_turma = soma_notas / n_alunos

    # --- SAÍDA ---
    print("\n--- RESUMO DA TURMA ---")
    print(f"Maior Nota: {maior_nota:.1f}")
    print(f"Menor Nota: {menor_nota:.1f}")
    print(f"Média da Turma: {media_turma:.2f}")
    print(f"Aprovados: {aprovados}")
    print(f"Em Recuperação: {recuperacao}")
    print(f"Reprovados: {reprovados}")

if __name__ == "__main__":
    main()