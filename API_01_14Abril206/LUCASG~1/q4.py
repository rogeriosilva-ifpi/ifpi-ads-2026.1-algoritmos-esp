def validar_notas(nota):
    if nota >=0 and nota <= 10:
        return True
    else:
        return print('Nota inválida')




def main():
    qtd_alunos = int(input('Informe a quantidade de alunos: '))
    maior_nota = 0
    menor_nota = 999
    qtd_alunos_aprovados = 0
    qtd_alunos_recuperacao = 0
    qtd_alunos_reprovado = 0
    somatorio = 0

    while qtd_alunos > 0:
        nota = int(input('Informe sua nota: '))
        somatorio += nota

        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota
        if nota >= 7:
            print('Aluno aprovado')
            qtd_alunos_aprovados += 1
        elif nota >= 5 and nota < 7:
            print('Aluno em recuperação')
            qtd_alunos_recuperacao += 1
        elif nota < 5:
            print('Aluno reprovado')
            qtd_alunos_reprovado += 1

        qtd_alunos -= 1
    print(f'A maior nota foi {maior_nota}')
    print(f'A menor nota foi {menor_nota}')
    ### PROFESSOR TENTEI FAZER DE TODAS AS FORMAS, MAS NESSE PRINT OQUE QUERIA ERA PEGAR O SOMATORIO DAS NOTAS E DIVIDIR PELA QUANTIDADE DE ALUNOS
    ###print(f'A media da turma foi {somatorio}')
    print(f'A quantidade de alunos aprovados foi de {qtd_alunos_aprovados}')
    print(f'A quantidade de alunos em recuperacao foi de {qtd_alunos_recuperacao}')
    print(f' A quantidade alunos reprovados foi {qtd_alunos_reprovado}')



main()

