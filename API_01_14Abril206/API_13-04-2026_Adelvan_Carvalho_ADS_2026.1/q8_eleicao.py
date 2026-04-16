from utils import obter_inteiro

def exibir_resultado(votos):
    # --- PROCESSAMENTO ---
    total_validos = sum(votos[1:5])
    brancos = votos[0]
    nulos = votos[5]
    
    vencedor_votos = -1
    vencedores = []
    
    # --- SAÍDA ---
    print("\n--- RESULTADO DA ELEIÇÃO ---")
    print(f"Total de Votos Válidos: {total_validos}")
    print(f"Votos Brancos: {brancos}")
    print(f"Votos Nulos: {nulos}")
    
    # Processamento de cada candidato e identificação do vencedor
    for i in range(1, 5):
        percentual = (votos[i] / total_validos * 100) if total_validos > 0 else 0
        print(f"Candidato {i}: {votos[i]} votos ({percentual:.2f}%)")
        
        if votos[i] > vencedor_votos:
            vencedor_votos = votos[i]
            vencedores = [i]
        elif votos[i] == vencedor_votos and votos[i] > 0:
            vencedores.append(i)

    # Verificação de Segundo Turno e Vencedor
    if total_validos > 0:
        maior_percentual = (vencedor_votos / total_validos) * 100
        
        if len(vencedores) > 1:
            print(f"Empate entre os candidatos: {vencedores}")
            print("Haverá SEGUNDO TURNO.")
        elif maior_percentual <= 50:
            print(f"Vencedor atual: Candidato {vencedores[0]}")
            print("Haverá SEGUNDO TURNO (nenhum candidato atingiu mais de 50%).")
        else:
            print(f"Vencedor: Candidato {vencedores[0]}")

def main():
    # --- ENTRADA ---
    # Índice 0: Branco, 1-4: Candidatos, 5: Nulo
    votos = [0] * 6 
    
    while True:
        print("\nMENU: 1-Votar | 2-Ver Resultado | 3-Encerrar")
        opcao = obter_inteiro("Escolha uma opção: ")
        
        # --- PROCESSAMENTO / ENTRADA ---
        if opcao == 1:
            voto = obter_inteiro("Voto (1-4 Candidatos, 0-Branco, 5-Nulo): ")
            if 0 <= voto <= 5:
                votos[voto] += 1
                print("Voto registrado!")
            else:
                print("Erro: Opção de voto inválida!")
                
        elif opcao == 2:
            exibir_resultado(votos)
            
        elif opcao == 3:
            print("Encerrando sistema de votação...")
            break
        else:
            print("Erro: Opção de menu inválida!")

if __name__ == "__main__":
    main()