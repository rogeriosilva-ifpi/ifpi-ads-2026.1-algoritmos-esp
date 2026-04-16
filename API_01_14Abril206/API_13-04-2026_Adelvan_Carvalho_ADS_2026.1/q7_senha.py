from utils import obter_texto

def validar_senha(senha):
    # --- PROCESSAMENTO ---
    # Regra: Deve ter exatamente 6 dígitos e ser numérica 
    if len(senha) != 6 or not senha.isdigit():
        return False, "A senha deve conter exatamente 6 dígitos numéricos."
    
    # Regra: O primeiro dígito não pode ser zero 
    if senha[0] == '0':
        return False, "Regra violada: O primeiro dígito não pode ser zero."
    
    soma = 0
    for i in range(len(senha)):
        digito_atual = int(senha[i])
        soma += digito_atual
        
        # Regra: Não pode ter dois dígitos iguais consecutivos 
        if i > 0:
            if senha[i] == senha[i-1]:
                return False, "Regra violada: Não pode ter dois dígitos iguais consecutivos."
                
    # Regra: A soma dos dígitos deve ser maior que 20 
    if soma <= 20:
        return False, f"Regra violada: A soma dos dígitos ({soma}) deve ser maior que 20."
    
    return True, "Senha cadastrada com sucesso!"

def main():
    # --- ENTRADA ---
    while True:
        # Peça a senha e valide [cite: 57]
        senha_candidata = obter_texto("Cadastre sua senha de 6 dígitos: ")
        
        # --- PROCESSAMENTO ---
        valida, mensagem = validar_senha(senha_candidata)
        
        # --- SAÍDA ---
        if valida:
            print(f"\nConfirmação: {mensagem}") # 
            break
        else:
            # Se inválida, informe qual regra foi violada e peça novamente [cite: 57]
            print(f"Erro: {mensagem}")

if __name__ == "__main__":
    main()