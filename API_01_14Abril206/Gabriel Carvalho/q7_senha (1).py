def main():

    valida = 0

    while valida == 0:
        senha = input("Digite uma senha numérica de 6 dígitos: ")

        erro = 0

        
        if len(senha) != 6:
            print("Erro: A senha deve ter exatamente 6 dígitos.")
            erro = 1
        else:
            
            i = 0
            while i < 6:
                if senha[i] < '0' or senha[i] > '9':
                    print("Erro: A senha deve conter apenas números.")
                    erro = 1
                    i = 6  
                else:
                    i = i + 1

            
            if erro == 0 and senha[0] == '0':
                print("Erro: O primeiro dígito não pode ser 0.")
                erro = 1

            
            if erro == 0:
                i = 0
                while i < 5:
                    if senha[i] == senha[i + 1]:
                        print("Erro: Não pode haver dígitos iguais consecutivos.")
                        erro = 1
                        i = 5  
                    else:
                        i = i + 1

            
            if erro == 0:
                soma = 0
                i = 0
                while i < 6:
                    soma = soma + int(senha[i])
                    i = i + 1

                if soma <= 20:
                    print("Erro: A soma dos dígitos deve ser maior que 20.")
                    erro = 1

        
        if erro == 0:
            print("Senha cadastrada com sucesso!")
            valida = 1

main()