# Criar um sistema bancário
# Fazer 3 operações: depósito, saque, extrato
# Depósito: Deve ser possível só depositar valores positivos; tem apenas 1 usuário; Todos os depósitos devem
# ser armazenados em uma única variável e exibidos na extração de extrato.

# Saque: limite diário de 3 saques no máximo em R$ 500,00 por saque. Exibir mensagem informando se o usuário
# não tem saldo; Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Extrato: Deve listar todos os depósitos e saques realizados na conta. Mostrar o saldo final em "R$ XXX.XX".

from func_bancarias import banco

menu = """
Escolhe uma opção para prosseguir:

D = "Deposito"
S = "Saque"
E = "Extrato"
Q = "Sair"
"""

agencia = "0001"
conta = "0001"
saldo = 0
qtd_saque_efetuado = 0
historico_deposito = ""
historico_saque = ""


banco = banco(agencia, conta, saldo ,qtd_saque_efetuado, historico_deposito, historico_saque)

while True:
    opcao = str(input(menu)).upper()
    
    if opcao == "D":
        banco.deposito()
                    
    elif opcao == "S":
        banco.saque()
    elif opcao == "E":
        banco.extrato()        
    elif opcao == "Q":
        break
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
        