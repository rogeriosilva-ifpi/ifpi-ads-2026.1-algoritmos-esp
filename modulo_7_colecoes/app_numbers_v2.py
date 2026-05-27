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
    5 - Listar somente ímpares (Filter)
    6 - Listar somente pares (Filter)
    7 - Multiplicar números por N (Map)
    8 - Listar o Triplo dos números ímpares (Map/Filter)
    9 - Listar somente positivos (Filter)
    10 - Listar somente negativos (Filter)
    11 - Listar a metade dos negativos (Filter/Map)
    12 - Mostrar o Resto da divisão por 2 (Map)
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
        elif opcao == 5:
            numeros_impares = filtrar(numeros, eh_impar)
            listar_numeros(numeros_impares)
            sucesso()
        elif opcao == 6:
            numeros_pares = filtrar(numeros, lambda x:x%2==0)
            numeros_pares = filtrar(numeros, eh_par)
            listar_numeros(numeros_pares)
            sucesso()
        elif opcao == 7:
            n = int(input('Multiplicar por: '))
            numeros_mapeados = mapear(numeros, lambda x:x*n)
            listar_numeros(numeros_mapeados)
            sucesso()
        elif opcao == 8:
            lista = mapear(filtrar(numeros, eh_impar), lambda x:x*3)
            listar_numeros(lista)
            sucesso()
        elif opcao == 9:
            positivos = filtrar(numeros, eh_positivo)
            listar_numeros(positivos)
            sucesso()
        elif opcao == 10:
            # negativos = filtrar(numeros, lambda n:n<0)
            negativos = filtrar(numeros, eh_negativo)
            listar_numeros(negativos)
            sucesso()
        elif opcao == 11:
            lista = mapear(filtrar(numeros, lambda x:x<0), lambda r:r*0.5)
            listar_numeros(lista)
            sucesso()
        elif opcao == 12:
            lista = mapear(numeros, lambda x:x%2)
            listar_numeros(lista)
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


# Funcao Critério
def eh_impar(numero): # lambda numero:numero%2 != 0
    return numero % 2 != 0


def eh_par(numero):
    return not eh_impar(numero)


def eh_positivo(numero):
    return numero > 0


def eh_negativo(numero):
    return numero < 0

# Filter
def filtrar(colecao, criterio):
    lista = []
    for item in colecao:
        if criterio(item):
            lista.append(item)

    return lista


# Map
def mapear(colecao, transformacao):
    lista = []
    for item in colecao:
        lista.append(transformacao(item))
    
    return lista

def mapear_multiplicar(numeros, n):
    lista = []
    for numero in numeros:
        lista.append(numero*n)
    
    return lista


def mapear_resto_por_2(numeros):
    lista = []
    for numero in numeros:
        lista.append(numero % 2)
    
    return lista
    


def linha(tamanho):
    print(tamanho*'-')


main()