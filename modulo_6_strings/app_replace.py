def main():
    texto = input('Texto: ')
    substituido = input('Substituido: ')
    substituto = input('Substituto: ')

    texto_novo = replace(texto, substituido, substituto)

    print(texto_novo)


def replace(texto, a, b):
    texto_novo = ''
    
    for caracter in texto:
        if caracter == a:
            texto_novo = texto_novo + b
        else:
            texto_novo = texto_novo + caracter
    

    return texto_novo


main()