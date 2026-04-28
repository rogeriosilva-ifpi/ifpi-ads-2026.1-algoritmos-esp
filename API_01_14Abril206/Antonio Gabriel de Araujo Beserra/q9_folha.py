def ler_inteiro(mensagem, minimo):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
            else:
                print("Valor inválido")
        except ValueError:
            print("Valor inválido")


def ler_float(mensagem, minimo):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= minimo:
                return valor
            else:
                print("Valor inválido")
        except ValueError:
            print("Valor inválido")


qtd = ler_inteiro("Digite a quantidade de funcionários: ", 1)

for i in range(1, qtd + 1):
    nome = input(f"Digite o nome do funcionário {i}: ")

    salario = ler_float("Digite o salário bruto: ", 1632)
    horas_extras = ler_inteiro("Digite a quantidade de horas extras: ", 0)

    hora_normal = salario / 220
    valor_extra = hora_normal * 1.5
    total_extra = valor_extra * horas_extras

    inss = salario * 0.11

    if salario > 2000:
        ticket = 150
    else:
        ticket = 0

    liquido = salario + total_extra - inss - ticket

    print("\nEXTRATO")
    print(f"Nome: {nome}")
    print(f"Salário bruto: R$ {salario:.2f}")
    print(f"Horas extras: R$ {total_extra:.2f}")
    print(f"INSS: R$ {inss:.2f}")
    print(f"Vale refeição: R$ {ticket:.2f}")
    print(f"Salário líquido: R$ {liquido:.2f}\n")