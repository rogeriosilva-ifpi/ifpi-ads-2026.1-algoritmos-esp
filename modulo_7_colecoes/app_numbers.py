import os

def main():
    limpar_tela()
    numeros = carregar_numeros_arquivo()
    
    menu = '''
    |>>> APP Número <<<|
    1 - Novo número
    2 - Listar número
    3 - Atualizar número
    4 - Remover número
    --------------------
    0 - Sair >> '''

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            numero = int(input('Novo número: '))
            numeros.append(numero)
            sucesso()
        elif opcao == 2:
            listar_numeros(numeros)
            sucesso()

        elif opcao == 3:
            numero_atual = int(input('Número atual: '))
            while not contem_item(numeros, numero_atual):
                print(f'O número {numero_atual} não está na lista.')
                numero_atual = int(input('Número atual: '))

            novo_numero = int(input('Novo número: '))

            substituir_item(numeros, numero_atual, novo_numero)
            sucesso()
        elif opcao == 4:
            numero = int(input('Número atual: '))
            while not contem_item(numeros, numero):
                print(f'O número {numero} não está na lista.')
                numero = int(input('Número atual: '))

            numeros = remover_item(numeros, numero)
            sucesso()

        input('Enter para continuar...')
        limpar_tela()
        opcao = int(input(menu))
    
    # saindo
    gravar_dados(numeros)


def sucesso():
    print('Operação realizada com sucesso!')


def limpar_tela():
    os.system('clear') # 'cls'


def carregar_numeros_arquivo():
    numeros = []
    arquivo = open('numeros.txt', 'r')
    for linha in arquivo:
        numero = linha.strip()
        numeros.append(int(numero))

    arquivo.close()
    return numeros

def gravar_dados(numeros):
    linhas = []
    for numero in numeros:
        linhas.append(f'{numero}\n')
    
    arquivo = open('numeros.txt', 'w')
    arquivo.writelines(linhas)
    arquivo.close()


def contem_item(colecao, elemento):
    for item in colecao:
        if item == elemento:
            return True
    
    return False


def substituir_item(colecao, elemento, novo_elemento):
    for i in range(len(colecao)):
        if colecao[i] == elemento:
            colecao[i] = novo_elemento


def listar_numeros(numeros):
    print(f'>>> {len(numeros)} números Cadatrados <<<')
    linha(20)
    for numero in numeros:
        print(numero, end=' ')
    print()
    linha(20)


def remover_item(colecao, elemento):
    nova_colecao = []
    for item in colecao:
        if item != elemento:
            nova_colecao.append(item)
    
    return nova_colecao

    


def linha(tamanho):
    print(tamanho*'-')


main()