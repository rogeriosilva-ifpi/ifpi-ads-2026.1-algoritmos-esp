def ler_termo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Digite um número maior que 0")
        except ValueError:
            print("Valor inválido")

def ler_razao(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Digite um número maior que 0")
        except ValueError:
            print("Valor inválido")

def ler_quantidade_de_termos(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= 2:
                return valor
            else:
                print("Digite um valor maior ou igual a 2")
        except ValueError:
            print("Valor inválido")

def ler_sistema(mensagem):
    while True:
        valor = input(mensagem).upper()
        if valor in ("S","N"):
            return valor
        else:
            print("Digite (S/N)")

sistema = "S"

while sistema == "S":

    soma_total = 0

    primeiro_termo = ler_termo("Digite o primeiro termo: ")
    razao = ler_razao("Digite a razão: ")
    numero_de_termos = ler_quantidade_de_termos("Digite a quantidade de termos: ")

    for i in range(1 , numero_de_termos + 1):
        soma_total += primeiro_termo
        print(primeiro_termo)
        calculo = primeiro_termo + razao
        primeiro_termo = calculo

    media = soma_total / numero_de_termos

    print(f'Soma total: {soma_total}')
    print(f'Média: {media:.2f}')

    sistema = ler_sistema("Deseja realizar outra progrssao? (S/N): ")

