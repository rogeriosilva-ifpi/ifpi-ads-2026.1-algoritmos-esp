from utils_io import obter_inteiro

def main():
    a = obter_inteiro(f'\nDigite o 1 termo: ')
    r = obter_inteiro(f'Digite a razão: ')
    n = obter_inteiro(f'Digite o numero de termos (no mínimo 2): ')

    while n < 2:
        print(f'\nQuantidade de termos invalida!')
        n = obter_inteiro(f'Digite o numero de termos (no mínimo 2): ')

    digito_atual = a
    soma_termos = 0
    contador = 0

    print(f'{50*"-"}')

    print(f'Os termos dessa progressao são: ')
    while contador < n:
        soma_termos += digito_atual 
        digito_atual += r
        contador += 1
        print(digito_atual)

    media = calcular_media(soma_termos, n)

    print(f'>> A soma dos termos dessa progressao é: {soma_termos}')
    print(f'>> A media dessa progressao é: {media}')

def calcular_media(soma, n):
    media = soma/n
    return media


        


main()


        