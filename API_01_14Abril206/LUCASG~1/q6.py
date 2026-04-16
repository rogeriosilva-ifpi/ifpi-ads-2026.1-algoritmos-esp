
def main():
    qtd_termos = int(input('Quantidades de termos: '))
    primeiro_termo = int(input('Digite o primeiro termo: '))
    razao = int(input('Digite a razao: '))

    while qtd_termos > 0:
        termo = primeiro_termo + razao
        qtd_termos -= 1
        termo += razao
        print(termo)
main()