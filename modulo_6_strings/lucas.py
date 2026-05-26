def main():
    nome = input('Nome: ')

    nome_alta = upper(nome)

    print(nome_alta)


def upper(nome):
    novo_nome = ''
    for caracter in nome:
        codigo = ord(caracter)
        if codigo >= 97 and codigo <= 122:
            novo_codigo = codigo - 32
            novo_caracter = chr(novo_codigo)
            novo_nome += novo_caracter
        else:
            novo_nome += caracter
    
    return novo_nome


main()