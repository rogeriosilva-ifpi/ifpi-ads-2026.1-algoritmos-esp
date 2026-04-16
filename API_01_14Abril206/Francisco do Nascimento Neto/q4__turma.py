def main():

    n = int(input("Digite a quantidade de alunos da turma:"))
    soma = 0
    aprovados = 0
    recuperaco = 0
    reprovado = 0
    maior = -1
    menor = 11



    for i in range(n):
        nota = float(input("Digite a nota:"))

        if nota < 0 or nota > 10:
            print("Nota invalida")
        else:
            soma += nota  

            if nota > maior:
                maior = nota

            if nota < menor:
                menor = nota

            if nota >= 7:
                aprovados = aprovados + 1
            else:
                if nota >= 5:
                    recuperaco = recuperaco + 1
                else:
                    reprovado = reprovado + 1   

    media = soma / n

    print(f"Maior nota:{maior}")  
    print(f"Menor nota:{menor}")
    print(f"Média da turma:{media}")               
    print(f"Aprovador:{aprovados}")
    print(f"Recuperação:{recuperaco}")
    print(f"Reprovados:{reprovado}")

main()    