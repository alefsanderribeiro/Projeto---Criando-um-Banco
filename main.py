# Criar um sistema bancário
# Fazer 3 operações: depósito, saque, extrato
# Depósito: Deve ser possível só depositar valores positivos; tem apenas 1 usuário; Todos os depósitos devem
# ser armazenados em uma única variável e exibidos na extração de extrato.

# Saque: limite diário de 3 saques no máximo em R$ 500,00 por saque. Exibir mensagem informando se o usuário
# não tem saldo; Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Extrato: Deve listar todos os depósitos e saques realizados na conta. Mostrar o saldo final em "R$ XXX.XX".

import func_bancarias as fb

menu = """
Escolhe uma opção para prosseguir:

D = "Deposito"
S = "Saque"
E = "Extrato"
Q = "Sair"
"""

# Endereço: Logradouro, número - bairro - cidade/Sigla Estado.
# O CPF deve ter somente um número cadastrado, do tipo String.
dict_usuarios = {}

print(dict_usuarios)
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

user = fb.criar_usuario()
cpf = user[0]
dict_usuarios.update({cpf: user[1:5]})
nome = dict_usuarios[cpf][0] # como procurar o nome do cliente
data_nascimento = dict_usuarios[cpf][1] #como procurar a data do nascimento do cliente
endereco = dict_usuarios[cpf][2][0] #como procurar um endereço

    

    


""" banco = fb.banco(agencia, conta, saldo ,qtd_saque_efetuado, historico_deposito, historico_saque)

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
         """