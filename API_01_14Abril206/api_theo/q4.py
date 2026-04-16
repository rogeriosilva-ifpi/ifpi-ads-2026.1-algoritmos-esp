def main():
    alunos_totais = 0
    alunos_aprovados = 0
    alunos_recuperacao = 0
    alunos_reprovados = 0
    maior_nota = None
    menor_nota = None
    soma = 0

    while True:
        nota = validar_notas('Digite a nota do aluno (flag = 99): ')
        if nota == 99:
            break

        alunos_totais += 1
        soma += nota

        if nota >= 7:
            print('Aluno aprovado.')
            alunos_aprovados += 1
        elif nota >= 5:
            print('Aluno de recuperação.')
            alunos_recuperacao += 1
        else:
            print('Aluno reprovado.')
            alunos_reprovados += 1
        
        media = soma / alunos_totais

        if menor_nota is None or nota < menor_nota:
            menor_nota = nota
        if maior_nota is None or nota > maior_nota:
            maior_nota = nota

    print(f'Maior nota: {maior_nota}')
    print(f'Menor nota: {menor_nota}')
    print(f'Média da turma: {media:.2f}')
    print(f'Alunos totais: {alunos_totais}')
    print(f'Alunos aprovados: {alunos_aprovados}')
    print(f'Alunos recuperação: {alunos_recuperacao}')
    print(f'Alunos reprovados: {alunos_reprovados}')

def validar_notas(mensagem):
    try:
        numero = float(input(mensagem))
        if numero >= 0 and numero <= 10 or numero == 99:
            return numero
        else:
            print('Entrada inválida. Digite uma nota válida.')
            return validar_notas(mensagem)
        
    except ValueError:
        print('Entrada inválida. Digite um número')
        return validar_notas(mensagem)

main()