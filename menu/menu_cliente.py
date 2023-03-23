from pathlib import Path
import sys
sys.path.append(str(Path().absolute()))
import contas.cliente as fu
import autenticacao.autenticacao_conta as aut_conta
import autenticacao.autenticacao_senha as aut_senha


menu_usuario = """
Escolhe uma opção para prosseguir:


C = "Cadastro de novo usuário"
A = "Ativar Usuário"
D = "Desativar Usuário"
Q = "Sair"

"""


def menu_cliente():
    while True:
        
        while True:
            opcao_user = str(input(menu_usuario)).upper()
            
            # Caso a resposta for "C", será feiro o cadastro do usuário.
            if opcao_user == "C":
                CPF = str(input(("Digita o número de CPF:\n ")))
                user = fu.Cliente(CPF)
                verif = aut_conta.Verificacao().cadastro(CPF)
                if verif:
                    print("Usuário já cadastrado")
                
                else:
                    user.adicionar_usuario()
            # Caso a resposta for "A", será feiro a Ativação do usuário.
            elif opcao_user == "A":
                CPF = str(input(("Digita o número de CPF:\n ")))
                user = fu.Cliente(CPF)
                verif = aut_conta.Verificacao().cadastro(CPF)
                
                if verif:
                    user.ativar_usuario()
                else:
                    print("Usuário não cadastrado!")
                    
            # Caso a resposta for "D", será feiro a desativação do usuário
            elif opcao_user == "D":
                CPF = str(input(("Digita o número de CPF:\n ")))
                user = fu.Cliente(CPF)
                verif = aut_conta.Verificacao().cadastro(CPF)
                if verif:
                    user.desativar_usuario()
                else:
                    print("Usuário não cadastrado!")
                    
            # Caso a resposta for "Q", voltará para o menu principal.
            elif opcao_user == "Q":
                print("Sair")
                break
            
            else:
                print("Operação Inválida, por favor selecione novamente a operação desejada.")
        
            
        break