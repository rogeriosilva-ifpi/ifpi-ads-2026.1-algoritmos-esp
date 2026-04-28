def main():

    N = int(input('Digite um número inteiro: '))
    M = int(input('Digite um segundo número inteiro: '))

    i = N
    soma = 0
    encontrou = 0

    while i <= M:
        if i % 2 != 0:
            if i % 3 == 0:
                print(i)
                soma = soma + i 
                encontrou = 1
        i = i + 1

    if encontrou == 1:
        print('Soma', soma)
    else:
        print('Nenhum número satisfaz a condição')


main()
               



