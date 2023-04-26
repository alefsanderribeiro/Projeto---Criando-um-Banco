# Criar um sistema bancário
# Fazer 3 operações: depósito, saque, extrato
# Depósito: Deve ser possível só depositar valores positivos; tem apenas 1 usuário; Todos os depósitos devem
# ser armazenados em uma única variável e exibidos na extração de extrato.

# Saque: limite diário de 3 saques no máximo em R$ 500,00 por saque. Exibir mensagem informando se o usuário
# não tem saldo; Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Extrato: Deve listar todos os depósitos e saques realizados na conta. Mostrar o saldo final em "R$ XXX.XX".


import menu.menu_cliente as m_cliente
import menu.menu_conta as m_conta
import logs
import relatorios
import transacoes


menu_principal = """
Escolhe uma opção para prosseguir:


U = "Usuário"
C = "Conta Bancária"
Q = "Sair"

"""


while True:
    opcao = str(input(menu_principal)).upper()
    
    if opcao == "U":
        m_cliente.menu_cliente()

    elif opcao == "C":
        m_conta.menu_conta()
        
    elif opcao == "Q":
        break
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")


