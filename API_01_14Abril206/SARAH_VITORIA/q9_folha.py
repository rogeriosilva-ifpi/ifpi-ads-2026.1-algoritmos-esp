from utils_io import obter_inteiro, obter_texto, obter_float

def main():
    n_funcionarios = obter_inteiro(f'\nNúmero de funcionarios: ')

    contador = 0


    while contador < n_funcionarios:
        contador += 1
        nome = obter_texto(f'Nome do funcionario {contador}: ')
        salario_bruto = obter_float(f'Digite o salario bruto: ')
        hr_extra = obter_inteiro(f'Digite a quantidade de horas extras: ')

        valor_hr_extra = calcular_valor_hr_extra(salario_bruto, hr_extra)
        inss = calcular_inss(salario_bruto)
        vale_ref = calcular_vale(salario_bruto)
        salario_liquido = calcular_salario_lqd(salario_bruto, inss, hr_extra)

        extrato = f'''\n
--- EXTRATO: {nome} ---
SALARIO BRUTO:      \tR$ {salario_bruto:.2f}
HORAS EXTRAS:       \tR$ {valor_hr_extra:.2f} ({hr_extra}h)
INSS:               \tR$ {inss:.2f}
VALE REFEICAO:      \tR$ {vale_ref:.2f}
SALARIO LIQUIDO:    \tR$ {salario_liquido:.2f}

'''
        print(extrato)

def calcular_salario_lqd(salario_bruto, inss, hr_extra):
    salario_bruto -= inss+hr_extra
    return salario_bruto

def calcular_vale(salario_bruto):
    if salario_bruto > 2000:
        vale = 150
        return vale
    else:
        vale = 0
        return vale

def calcular_inss(salario_bruto):
    inss = salario_bruto*0.11
    return inss

def calcular_valor_hr_extra(salario_bruto, hr_extra ):
    hr_normal = hr_normal = salario_bruto / 220
    valor_hr_extra = (hr_normal + (hr_normal*1.5))*hr_extra
    return valor_hr_extra




main()