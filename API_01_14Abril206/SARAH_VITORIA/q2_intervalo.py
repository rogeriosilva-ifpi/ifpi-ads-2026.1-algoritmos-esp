from utils_io import obter_inteiro

def main():
    n = obter_inteiro(f'Limite superior: ')
    m = obter_inteiro(f'Limite inferior: ')

    numero = f''
    soma = 0
    for i in range(n, m+1):
        if (i % 3 == 0) and (i % 2 != 0):
            numero += f' {i}'
            soma += i
        
    if numero == '':
        print(f'Nenhum número neste intervalo satisfaz a condição')
    else:
        print(f'Numero:{numero}')
        print(f'Soma: {soma}')

main()