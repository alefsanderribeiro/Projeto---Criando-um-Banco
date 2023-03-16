# Criar um sistema bancário
# Fazer 3 operações: depósito, saque, extrato
# Depósito: Deve ser possível só depositar valores positivos; tem apenas 1 usuário; Todos os depósitos devem
# ser armazenados em uma única variável e exibidos na extração de extrato.

# Saque: limite diário de 3 saques no máximo em R$ 500,00 por saque. Exibir mensagem informando se o usuário
# não tem saldo; Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Extrato: Deve listar todos os depósitos e saques realizados na conta. Mostrar o saldo final em "R$ XXX.XX".

import contas.conta as fb
import contas.cliente as fu
import banco_de_dados
import autenticacao.autenticacao as aut
import autenticacao.segurança as seg
import logs
import relatorios
import transacoes


menu_principal = """
Escolhe uma opção para prosseguir:


U = "Usuário"
C = "Conta Bancária"
Q = "Sair"

"""

menu_usuario = """
Escolhe uma opção para prosseguir:


C = "Cadastro de novo usuário"
A = "Ativar Usuário"
D = "Desativar Usuário"
Q = "Sair"

"""


menu_conta = """
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

while True:
    opcao = str(input(menu_principal)).upper()
    
    if opcao == "U":
        while True:
            
            while True:
                opcao_user = str(input(menu_usuario)).upper()
                
                # Caso a resposta for "C", será feiro o cadastro do usuário.
                if opcao_user == "C":
                    CPF = str(input(("Digita o número de CPF:\n ")))
                    user = fu.Cliente(CPF)
                    verif = aut.cadastro(CPF)
                    if verif:
                        print("Usuário já cadastrado")
                    
                    else:
                        user.adicionar_usuario()
                # Caso a resposta for "A", será feiro a Ativação do usuário.
                elif opcao_user == "A":
                    CPF = str(input(("Digita o número de CPF:\n ")))
                    user = fu.Cliente(CPF)
                    verif = aut.cadastro(CPF)
                    
                    if verif:
                        user.ativar_usuario()
                    else:
                        print("Usuário não cadastrado!")
                        
                # Caso a resposta for "D", será feiro a desativação do usuário
                elif opcao_user == "D":
                    CPF = str(input(("Digita o número de CPF:\n ")))
                    user = fu.Cliente(CPF)
                    verif = aut.cadastro(CPF)
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

    elif opcao == "C":
        

        while True:
            
            while True:
                opcao_conta = str(input(menu_conta)).upper()
                
                # Caso a resposta for "C", será feiro o cadastro do usuário.
                if opcao_conta == "C":
                    CPF = str(input(("Digita o seu número de CPF:\n ")))
                    user = fu.Cliente(CPF)
                    verif = aut.cadastro(CPF)
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
                    verif = aut.contas(cpf_ou_conta)
                    if verif == "":
                        print("Nada foi encontrado no nosso banco de dados. Por favor, revise os dados fornecidos.")
                    else:
                        numero_conta = str(input(("Digita o número da Conta que deseja alterar senha.\n ")))
                        resultado = seg.Senha(numero_conta).alterar_senha()
                        #banco.alterar_senha(conta)
 
                # Caso a resposta for "Q", voltará para o menu principal.
                elif opcao_conta == "Q":
                    print("Sair")
                    break
                
                else:
                    print("Operação Inválida, por favor selecione novamente a operação desejada.")
        
            break

              
    elif opcao == "Q":
        break
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
