from utils_io import obter_inteiro_minimo, obter_inteiro_positivo
import os


def main():
  limpar_tela()
  numero = 10

  opcao = obter_inteiro_minimo(menu(numero), 0)

  while opcao != 0:
    if opcao == 1:
      numero = obter_inteiro_positivo('Novo número: ')
      print('Número alterado com sucesso!')
    elif opcao == 2:
      binario = conveter_dec_binario(numero)
      print(f'O número {numero} em binário é {binario}')
    elif opcao == 3:
      print('O usuário quer em Octal')
    elif opcao == 4:
      print('O usuário quer em hexadecimal.')
    else:
      print('Opção inválida!')
    
    input('Enter para continuar...')
    limpar_tela()
    opcao = obter_inteiro_minimo(menu(numero), 0)

  limpar_tela()


def limpar_tela():
  os.system('clear')


def menu(numero: int):
  return f'''
  *** Conversor Número ***
  ------------------------
  1 - Alterar número (atual: {numero})
  2 - Exibir em Binário
  3 - Exibir em Octal
  4 - Exibir em Hexadecimal
  -------------------------
  0 - sair >> '''


def conveter_dec_binario(numero):
  quociente = numero // 2
  resto = numero % 2

  binario = str(resto)

  while quociente > 1:
    resto = quociente % 2
    quociente = quociente // 2

    binario = str(resto) + binario
  
  return str(quociente) + binario


main()