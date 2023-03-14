# Criar um sistema bancário
# Fazer 3 operações: depósito, saque, extrato
# Depósito: Deve ser possível só depositar valores positivos; tem apenas 1 usuário; Todos os depósitos devem
# ser armazenados em uma única variável e exibidos na extração de extrato.

# Saque: limite diário de 3 saques no máximo em R$ 500,00 por saque. Exibir mensagem informando se o usuário
# não tem saldo; Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Extrato: Deve listar todos os depósitos e saques realizados na conta. Mostrar o saldo final em "R$ XXX.XX".

import func_banc as fb
import func_user as fu


menu_principal = """
Escolhe uma opção para prosseguir:


U = "Usuário"
D = "Deposito"
S = "Saque"
E = "Extrato"
Q = "Sair"

"""

menu_usuario = """
Escolhe uma opção para prosseguir:


C = "Cadastro de novo usuário"
A = "Ativar Usuário"
D = "Desativar Usuário"
Q = "Sair"

"""

# Endereço: Logradouro, número - bairro - cidade/Sigla Estado.
# O CPF deve ter somente um número cadastrado, do tipo String.


# conta da agencia não pode ter o mesmo número. O número é sequenciado, começando com o número 1.
# agencia é fixa: "0001"
# uma conta não existe sem estar vinculado ao usuário
# não tem restrição de ter várias contas para o mesmo usuário

agencia = "0001"
conta = 0
saldo = 0
qtd_saque_efetuado = 0
historico_deposito = ""
historico_saque = ""


# dados = ["01912841223", "Alefsander Ribeiro", "23/10/1994", "R. Escorpião, n° 11700 - Bairro: Ulisses Guimarães - Porto Velho/RO."]
# dados1 = ["0191284122f1233", "Alefsander Ribeiro", "23/10/1994", "R. Escorpião, n° 11700 - Bairro: Ulisses Guimarães - Porto Velho/RO."]
# dados2 = ["04240084245", "Geissilaine Verônica", "19/107/1998", "R. Maué, n° 4445 - Bairro: Socialista - Porto Velho/RO."]
# dados3 = ["123461365123", "Alefsander Ribeiro", "23/10/1994", "R. Escorpião, n° 11700 - Bairro: Ulisses Guimarães - Porto Velho/RO."]
# dados4 = ["123461365", "Alefsander Ribeiro", "23/10/1994", "R. Escorpião, n° 11700 - Bairro: Ulisses Guimarães - Porto Velho/RO."]

#dados = fb.usuario(dados[0], dados[1], dados[2], dados[3])


#print(dados.verficar_cadastro())
#usuario.ativar_usuario("01912841223")


banco = fb.banco(agencia, conta, saldo ,qtd_saque_efetuado, historico_deposito, historico_saque)

while True:
    opcao = str(input(menu_principal)).upper()
    
    if opcao == "U":
        while True:
            
            while True:
                opcao_user = str(input(menu_usuario)).upper()
                
                # Caso a resposta for "C", será feiro o cadastro do usuário.
                if opcao_user == "C":
                    CPF = fu.usuario(str(input(("Digita o número de CPF:\n "))))
                    user = fu.usuario.verficar_cadastro(CPF)
                    if user:
                        print("Usuário já cadastrado")
                    
                    else:
                        CPF.adicionar_usuario()
                # Caso a resposta for "A", será feiro a Ativação do usuário.
                elif opcao_user == "A":
                    CPF = fu.usuario(str(input(("Digita o número de CPF:\n "))))
                    user = fu.usuario.verficar_cadastro(CPF)
                    
                    if user:
                        CPF.ativar_usuario()
                    else:
                        print("Usuário não cadastrado!")
                        
                # Caso a resposta for "D", será feiro a desativação do usuário
                elif opcao_user == "D":
                    CPF = fu.usuario(str(input(("Digita o número de CPF:\n "))))
                    user = fu.usuario.verficar_cadastro(CPF)
                    if user:
                        CPF.desativar_usuario()
                    else:
                        print("Usuário não cadastrado!")
                        
                # Caso a resposta for "Q", voltará para o menu principal.
                elif opcao_user == "Q":
                    print("Sair")
                    break
                
                else:
                    print("Operação Inválida, por favor selecione novamente a operação desejada.")
            
                
            break

    elif opcao == "D":
        banco.deposito()
                    
    elif opcao == "S":
        banco.saque()
    elif opcao == "E":
        banco.extrato()        
    elif opcao == "Q":
        break
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
