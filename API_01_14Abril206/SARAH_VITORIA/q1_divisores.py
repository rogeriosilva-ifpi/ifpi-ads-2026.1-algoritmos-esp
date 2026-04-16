from utils_io import obter_inteiro

def main():
    n = obter_inteiro(f'Digite um número: ')

    contador_divisores = 0
    divisores = f''
    for i in range(1, n+1):
        if (n % i == 0):
            divisores += f' {i}'
            contador_divisores += 1
    
    print(f'Divisores:{divisores}')
    print(f'Total: {contador_divisores} divisores')
    

main()