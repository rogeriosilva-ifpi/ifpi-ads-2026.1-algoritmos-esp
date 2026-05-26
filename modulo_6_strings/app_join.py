def main():
    texto = input('frase: ')
    novo_item = input('digite o que deseja adicionar como quebra: ')

    novo_texto = join(texto, novo_item)

    print(novo_texto)

def join(texto, novo_item):
    novo_texto = ''
    for caractere in texto:
        quebra = ' '
        if caractere != quebra:
            novo_texto += caractere
        else:
            novo_texto += novo_item

    return novo_texto

main()