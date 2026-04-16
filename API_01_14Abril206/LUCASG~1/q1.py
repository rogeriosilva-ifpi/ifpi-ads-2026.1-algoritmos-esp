def validar_numero_positivo(numero):
    if numero >= 0:
        print('Número válido')
    else:
        return print('Número inválido, renicie o sistema')



def main():
    numero = int(input("Digite um numero positivo: "))
    validar_numero_positivo(numero)


    for divisor in range(1,numero + 1,1):
        if numero % divisor == 0:
            print(divisor)
main()