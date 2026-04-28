def ler_senha(mensagem):
    while True:

        valor = input(mensagem)

        if len(valor) != 6:
            print("senha só pode ter 6 digitos")
            continue
        
        if not valor.isdigit():
            print("senha só pode ter numero")
            continue
        
        if valor[0] == "0":
            print("senha não pode começar com digito 0")
            continue
        
        soma_digitos = 0
        for i in valor:
            soma_digitos += int(i)
        
        if soma_digitos <= 20:
            print("A soma dos digitos da senha deve ser maior que 20")
            continue
        
        sequencia = True
        sequencia_decrecente = True

        for i in range(len(valor) - 1):
            atual = int(valor[i])
            proximo = int(valor[i + 1])

            if proximo - atual != 1:
                sequencia = False
            
            if atual - proximo != 1:
                sequencia_decrecente = False
            
        if sequencia_decrecente or sequencia:
            print("A senha não pode ter sequência numerica")
            continue
        
        return valor

senha = ler_senha("Digite a senha: ")
print(f'Senha: {senha}')
