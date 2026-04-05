cpf = input(f"Digite o seu CPF (apenas números):") 

if len(cpf) == 11 and cpf.isdigit(): 
    print("CPF válido.")

else:
    print("Erro: O CPF deve conter 11 dígitos numéricos.")