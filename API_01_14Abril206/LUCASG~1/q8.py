def showmenu():
    print('''
    1 - Votar
    2 - Ver resultado
    3 - Encerrar
    
    ''')















def main():
    qtd_votos = int(input('Informe quantos votos irão ser apurados: '))
    voto_1 = 0
    voto_2 = 0
    voto_3 = 0
    voto_4 = 0
    voto_branco = 0
    voto_nulo = 0
    votos_validos = 0
    votos_nulos_brancos = 0
    while qtd_votos > 0:
        showmenu()
        opcao = int(input('Qual das opções deseja seguir: '))
        if opcao == 1:
            voto = int(input('Digite seu voto de 0 a 5, lembrando que 0 são votos brancos e 5 para nulos'))
            if voto == 0:
                voto_branco += 1
                votos_nulos_brancos += 1
            elif voto == 1:
                voto_1 += 1
                votos_validos += 1
            elif voto == 2:
                voto_2 += 1
                votos_validos += 1
            elif voto == 3:
                voto_3 += 1
                votos_validos += 1
            elif voto == 4:
                voto_4 += 1
                votos_validos += 1
            elif voto == 5:
                voto_nulo += 1
                votos_nulos_brancos += 1

            qtd_votos -= 1

        elif opcao == 2:
            print(f'A porcentagem de votos válidos {votos_validos + votos_nulos_brancos}')
            print(f'A porcentagem de votos no primeiro candidato {voto_1 * 100 / votos_validos}')
            print(f'A porcentagem de votos no segundo candidato {voto_2 * 100 / votos_validos}')
            print(f'A porcentagem de  votos no terceiro candidato {voto_3 * 100 / votos_validos}')
            print(f'A porcentagem de votos no quarto candidato {voto_4 * 100 / votos_validos}')
            print(f'A quantidade votos nulos {voto_nulo}')
            print(f'A quantidade de votos em branco {voto_branco}')
        elif opcao == 3:
            break
    print()














