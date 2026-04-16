def main():
    n = validar_entrada('Digite um número: ')
    i = 1
    total = 0

    while i <= n:
        if n % i == 0:
            print(f'Divisores: {i}')
            total += 1
        i += 1
        
    print(f'Total: {total}')

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