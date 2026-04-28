def main():

    n = int(input("Digite a quantidade de alunos: "))

    contador = 0

    maior_nota = -1
    menor_nota = 11
    soma = 0

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    while contador < n:
        nota = float(input(f"Digite a nota do aluno {contador + 1}: "))

        
        if nota > maior_nota:
            maior_nota = nota

        if nota < menor_nota:
            menor_nota = nota

        
        soma = soma + nota

        
        if nota >= 7:
            print("Situação: Aprovado")
            aprovados = aprovados + 1
        elif nota >= 5:
            print("Situação: Recuperação")
            recuperacao = recuperacao + 1
        else:
            print("Situação: Reprovado")
            reprovados = reprovados + 1

        contador = contador + 1

    media = soma / n

    print("\n--- Resultados ---")
    print("Maior nota:", maior_nota)
    print("Menor nota:", menor_nota)
    print("Média da turma:", media)
    print("Aprovados:", aprovados)
    print("Recuperação:", recuperacao)
    print("Reprovados:", reprovados)

main()