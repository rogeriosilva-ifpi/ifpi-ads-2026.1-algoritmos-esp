def obter_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

def obter_inteiro_positivo(mensagem):
    while True:
        valor = obter_inteiro(mensagem)
        if valor > 0:
            return valor
        print("Erro: Digite um número maior que zero.")

def obter_float(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(',', '.'))
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

def obter_float_faixa(mensagem, minimo, maximo):
    while True:
        valor = obter_float(mensagem)
        if minimo <= valor <= maximo:
            return valor
        print(f"Erro: O valor deve estar entre {minimo} e {maximo}.")

def obter_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Erro: O campo não pode ficar vazio.")

def obter_confirmacao(mensagem):
    while True:
        resp = obter_texto(mensagem).upper()
        if resp in ['S', 'N']:
            return resp == 'S'
        print("Erro: Digite S para Sim ou N para Não.")
        