def main():
    n = validar_entrada('Digite o N: ')
    m = validar_entrada('Digite o M: ')

    soma = 0

    if m > n:
        while n <= m:
            if n % 2 == 1 and n % 3 == 0:
                print(n)
                soma += n
            n += 1
        print(f'Soma: {soma}')
    else:
        print('Erro.')
        
def validar_entrada(mensagem):
    try:
        numero = int(input(mensagem))


        if numero > 0:
            return numero
        else:
            print('Entrada inválida. Digite um número positivo.')
            return validar_entrada(mensagem)
        
    except ValueError:
        print('Entrada inválida. Digite um número')
        return validar_entrada(mensagem)
main()