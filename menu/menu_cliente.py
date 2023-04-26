from pathlib import Path
import sys
sys.path.append(str(Path().absolute()))
import contas.cliente as fu
import autenticacao.autenticacao_conta as aut_conta
import autenticacao.autenticacao_senha as aut_senha


menu_usuario_com_cadastro = """
Escolhe uma opção para prosseguir:

A = "Ativar Usuário"
D = "Desativar Usuário"
E = "Excluir Usuário"
Q = "Sair"

"""

menu_usuario_sem_cadastro = """
Escolhe uma opção para prosseguir:


C = "Cadastro de novo usuário"
A = "Ativar Usuário"
D = "Desativar Usuário"
Q = "Sair"

"""


def menu_cliente():
    while True:
        
        cpf = str(input(("Digita o número de CPF:\n ")))
        verif = aut_conta.Verificacao().cadastro(cpf)

        while True:
            
            if verif == True:
                opcao_user = str(input(menu_usuario_com_cadastro)).upper()
                
                # Caso a resposta for "A", será feito a Ativação do usuário.
                if opcao_user == "A":   
                    user = fu.Cliente(cpf).alterar_status(ativado_ou_desativado="Ativado")
                    print(user)
                # Caso a resposta for "D", será feito a Desativação do usuário
                elif opcao_user == "D":
                    user = fu.Cliente(cpf).alterar_status(ativado_ou_desativado="Desativado")

                elif opcao_user == "E":
                    print("Excluindo o usário...")
                    
                # Caso a resposta for "Q", voltará para o menu principal.
                elif opcao_user == "Q":
                    print("Sair")
                    break
                
                else:
                    print("Operação Inválida, por favor selecione novamente a operação desejada.")
                
                
            elif verif == False:
                opcao_user = str(input(menu_usuario_sem_cadastro)).upper()
                # Caso a resposta for "C", será feiro o cadastro do usuário.
                if opcao_user == "C":
                    fu.Cliente(cpf).adicionar_usuario()
                        
                # Caso a resposta for "Q", voltará para o menu principal.
                elif opcao_user == "Q":
                    print("Sair")
                    break
                
                else:
                    print("Operação Inválida, por favor selecione novamente a operação desejada.")
        
            
        break
    
    