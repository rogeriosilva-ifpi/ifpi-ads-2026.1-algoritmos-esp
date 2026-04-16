def main():
    n_funcionarios = int(input("Número de funcionarios: "))
    for i in range(n_funcionarios):
        nome = input("Digite seu nome: ")
        salario_bruto = int(input("Digite seu salario bruto: "))
        extra = int(input("Quantas horas extras voce trabalhou no mes? "))
        definicao(nome, salario_bruto, extra)
            


def definicao(salario_bruto, nome):
    n = nome
    hora_normal = salario_bruto // 220
    hora_extra = hora_normal * 150/100
    inss = salario_bruto * 11/100
    vr = 150
    salario_liquido = salario_bruto + hora_extra - inss - vr
    print(F'''------EXTRATO {n} ------ 
          SALARIO BRUTO:    R$ {salario_liquido}
          HORAS EXTRAS:     R$ {hora_extra}
          INSS              R$ {inss}
          VALE REFEIÇÃO     R$ {vr}
          SALARIO LIQUIDO   R$ {salario_liquido}''')




if __name__ == "__main__":
    main()