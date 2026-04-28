def ler_dois_inteiros(valor_minimo, valor_maximo):
    while True:
        try:
            valor1 = int(input(valor_minimo))
            valor2 = int(input(valor_maximo))

            if valor_maximo > valor_minimo:
                return valor1, valor2
            else:
                print("Valor máximo tem que ser maior que valor mínimo")
        except:
            print("Valor inválido")

soma = 0

numero_minimo, numero_maximo = ler_dois_inteiros(

    "Digite o primeiro número: ",
    "Digite o segundo número: "
)


for i in range(numero_minimo, numero_maximo + 1):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
        print(i)

if soma == 0:
    print("Nenhum número no intervalo fornecido é ímpar e divisível por 3 ao mesmo tempo")
else:
    print(f'Soma: {soma}')