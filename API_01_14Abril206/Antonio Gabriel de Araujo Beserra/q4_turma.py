def ler_notas(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0 and valor <= 10:
                return valor
            else:
                print("Digite uma nota entre 0 e 10")
        except ValueError:
            print("Valor inválido")

def ler_sistema(mensagem):
    while True:
        valor = input(mensagem).upper()
        if valor in ("S","N"):
            return valor
        else:
            print("Digite (S/N)")

maior_nota = None
menor_nota = None

total_alunos_reprovados = 0
total_alunos_recuperacao = 0
total_alunos_aprovados = 0

soma_notas = 0
quantidade_de_alunos = 0

sistema = "S"

while sistema == "S":

    nota = ler_notas("Digite a nota do aluno: ")

    soma_notas += nota
    quantidade_de_alunos += 1

    if nota < 5:
        total_alunos_reprovados += 1
        print("Reprovado")
    elif nota < 7:
        total_alunos_recuperacao += 1
        print("Recuperação")
    else:
        total_alunos_aprovados += 1
        print("Aprovado")
    
    if maior_nota is None or nota > maior_nota:
        maior_nota = nota
    
    if menor_nota is None or nota < menor_nota:
        menor_nota = nota
    
    sistema = ler_sistema("Deseja continuar lendo as notas? (S/N): ")

if quantidade_de_alunos > 0:
    media = soma_notas / quantidade_de_alunos
    print("____________Resultado____________\n")
    print(f'Média das notas: {media:.2f}')
    print(f'Maior nota: {maior_nota:.2f}')
    print(f'menor nota: {menor_nota:.2f}')
    print(f'Quantidade de alunos reprovados: {total_alunos_reprovados}')
    print(f'Quantidade de alunos em recuperação: {total_alunos_recuperacao}')
    print(f'total de alunos aprovados: {total_alunos_aprovados}')
else:
    print("nenhuma nota computada")