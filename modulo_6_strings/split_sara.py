def main():
    nome = input('Nome: ')
    c = input('Ponto de quebra: ')
    nome_split = split(nome, c)
    print(nome_split)


def split(nome, quebra):
    palavras = []
    nova_palavra = ''
    nome = nome + quebra

    for caractere in nome:
        if caractere != quebra:
            nova_palavra = nova_palavra + caractere
        else:
            palavras.append(nova_palavra)
            nova_palavra = ''
    
    return palavras

main()