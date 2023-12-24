# Criar um sistema bancário
# Fazer 3 operações: depósito, saque, extrato
# Depósito: Deve ser possível só depositar valores positivos; tem apenas 1 usuário; Todos os depósitos devem
# ser armazenados em uma única variável e exibidos na extração de extrato.

# Saque: limite diário de 3 saques no máximo em R$ 500,00 por saque. Exibir mensagem informando se o usuário
# não tem saldo; Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Extrato: Deve listar todos os depósitos e saques realizados na conta. Mostrar o saldo final em "R$ XXX.XX".

from menu import menu_cliente as m_cliente
from menu import menu_conta as m_conta
from interfaces.interface import interface as ui

import logs
import relatorios
import transacoes

from interfaces.rc_imagens import *


if __name__ == "__main__":
    ui()

menu_principal = """

####  Bem vindo ao seu Banco Digital  ####

Escolhe uma opção para prosseguir:


U = "Usuário"
C = "Conta Bancária"
Q = "Sair"



####  -------------------------------  ####
"""

logs.logging.info("Abrindo o programa e perguntando o que é para fazer.")
while True:
    
    opcao = str(input(menu_principal)).upper()
    logs.logging.info(f"Opção escolhida: {opcao}")
    if opcao == "U":
        logs.logging.info("Indo para a parte do cliente.")
        m_cliente.menu_cliente()

    elif opcao == "C":
        m_conta.menu_conta()
        
    elif opcao == "Q":
        break
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
        
        


