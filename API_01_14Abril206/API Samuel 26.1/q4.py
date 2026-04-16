def main():
    n_notas = int(input("Quantas notas dos alunos: "))
    for i in range(n_notas):
        nota = int(input("Qual foi sua nota: "))
        maior_nota = max(n_notas)
        media_turma = n_notas / nota
        situacao(nota)
        return maior_nota, media_turma


def situacao(nota):
    if nota >= 7.0:
        print("Aprovado!")
    elif nota >= 5.0 and nota < 7.0:
        print('Recuperacao')
    elif nota < 5.0:
        print("Reprovado")


if __name__ == "__main__":
    main()