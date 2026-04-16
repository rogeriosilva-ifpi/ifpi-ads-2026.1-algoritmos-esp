from utils_io import obter_texto, obter_float, obter_inteiro

def main():
    n_alunos = obter_inteiro(f'\nNúmero de alunos: ')

    contador = 0
    soma = 0

    while contador < n_alunos:
        contador += 1
        nota = obter_float(f'Aluno {contador}: ')
        soma += nota
        situacao = analisar_situacao(nota)
        print(situacao)

    media = media_turma(soma, nota)
    print(f'Media da turma: {media}')

def media_turma(soma, nota):
    media = soma/nota
    return media

def analisar_situacao(nota):
    if nota >= 7:
        situacao = 'Aprovado'
        return situacao
    elif nota >= 5:
        situacao = 'Recuperacao'
        return situacao
    elif nota < 5: 
        situacao = 'Reprovado'
        return situacao
    
main()