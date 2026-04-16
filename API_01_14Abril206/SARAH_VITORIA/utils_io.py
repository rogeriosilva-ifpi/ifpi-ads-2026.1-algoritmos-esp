def obter_texto(texto):
    caracteres = input(texto)
    return caracteres

def obter_inteiro(texto):
    numero = int(input(texto))
    while type(numero) != int:
        print(f'Você não digitou um número inteiro!')
        numero = int(input(texto))
    return numero

def obter_float(texto):
    numero = float(input(texto))
    while type(numero) != float:
        print(f'Você não digitou um número!')
        numero = float(input(texto))
    return numero

