from pathlib import Path
import sys
sys.path.append(str(Path().absolute()))
import contas.conta as fb
import contas.cliente as fu
import autenticacao.autenticacao_conta as aut_conta
import autenticacao.autenticacao_senha as aut_senha



menu_opcoes_conta = """
Escolhe uma opção para prosseguir:


C = "Cadastro de nova Conta"
E = "Extrato"
M = "Movimentação de valor"
A = "Ativar Conta"
D = "Desativar Conta"
T = "Trocar de Senha"
Q = "Sair"

"""

menu_mov_valor = """

Escolhe uma opção para prosseguir:


D = "Depósito"
S = "Saque"
T = "Transferir entre contas"
Q = "Sair"


"""

def menu_conta():
    while True:
        
        while True:
            opcao_conta = str(input(menu_opcoes_conta)).upper()
            
            # Caso a resposta for "C", será feiro o cadastro do usuário.
            if opcao_conta == "C":
                CPF = str(input(("Digita o seu número de CPF:\n ")))
                user = fu.Cliente(CPF)
                verif = aut_conta.Verificacao().cadastro(CPF)
                if verif:
                    print("Prosseguir com a criação da conta")
                    banco = fb.Conta()
                    conta = banco.criar_conta(CPF)
                    print(conta)
                
                else:
                    
                    print("Usuário não encontrado!")
                    
            elif opcao_conta == "E":
                pass
            
            
            # Caso a resposta for "A", será feiro a Ativação da conta.
            elif opcao_conta == "A":
                pass
            
            
            # Caso a resposta for "S", será feiro a Movimentação do valor da conta.
            elif opcao_conta == "M":
                pass
                while True:
                    opcao_conta_mov = str(input(menu_mov_valor)).upper()
                    if opcao_conta_mov == "D":
                        pass
                    elif opcao_conta_mov == "S":
                        pass
                    elif opcao_conta_mov == "T":
                        pass
                    elif opcao_conta_mov == "Q":
                        break
                    else:
                        print("Operação Inválida, por favor selecione novamente a operação desejada.")
                    
            # Caso a resposta for "D", será feiro a desativação da conta
            elif opcao_conta == "D":
                pass
            
            
            # Caso a resposta for "T", será feita a troca da senha
            elif opcao_conta == "T":
                cpf_ou_conta = str(input(("Digita o número de CPF ou o número da Conta:\n ")))
                banco = fb.Conta()
                verif = aut_conta.Verificacao().contas(cpf_ou_conta)
                if verif == "":
                    print("Nada foi encontrado no nosso banco de dados. Por favor, revise os dados fornecidos.")
                else:
                    numero_conta = str(input(("Digita o número da Conta que deseja alterar senha.\n ")))
                    resultado = aut_senha.Senha(numero_conta).alterar_senha()
                    #banco.alterar_senha(conta)

            # Caso a resposta for "Q", voltará para o menu principal.
            elif opcao_conta == "Q":
                print("Sair")
                break
            
            else:
                print("Operação Inválida, por favor selecione novamente a operação desejada.")
    
        break

              
