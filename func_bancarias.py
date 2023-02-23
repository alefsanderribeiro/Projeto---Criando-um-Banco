# Nesse arquivo ficará todas as funções bancárias e configurações do banco
from datetime import datetime

class banco:
    
    def __init__(self, agencia, conta, saldo: int, quantidade_saque_efetuado: int, historico_deposito, historico_saque):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.qtd_saque = quantidade_saque_efetuado
        self.historico_deposito = historico_deposito
        self.historico_saque = historico_saque
        self.LIMITE = {"Valor_Saque": 500, "Qtd_Saque": 3}
        
        
    def __str__(self):
        
        return "Este é um banco feito "
        
        

    def deposito(self):
        while True:
            valor_deposito = float(input("Insere o valor que deseja depositar:\n"))
            if valor_deposito > 0:
                self.saldo += valor_deposito
                self.historico_deposito += f"Depósito: R$ {valor_deposito:.2f}\n"
                print(F"Deposito no valor de {valor_deposito} feito com sucesso.\n")
                continuar = str(input("Deseja realizar mais um deposito? \n S ou N?")).upper()
                
                if continuar == "S":
                    continue
                elif continuar == "N":
                    break   
            else:
                print("Valor não permitido.")
        return self.saldo
        
    def saque(self):
        while True:
            valor_saque = float(input("Insere o valor que deseja sacar:\n"))
            if 0 < valor_saque <= self.LIMITE["Valor_Saque"] and self.qtd_saque < self.LIMITE["Qtd_Saque"]\
                and valor_saque <= self.saldo:
                self.saldo -= valor_saque
                self.historico_saque += f"Saque: R$ {valor_saque:.2f}\n"
                self.qtd_saque += 1
                print(f"Saque no valor de {valor_saque} feito com sucesso.\n")
                continuar = str(input("Deseja realizar mais um saque? \n S ou N?")).upper()
                if continuar == "S":
                    continue
                elif continuar == "N":
                    break
            elif valor_saque > self.LIMITE["Valor_Saque"]:
                print(f'Valor maior do que o limite de saque: {self.LIMITE["Valor_Saque"]}')
            elif self.qtd_saque == self.LIMITE["Qtd_Saque"]:
                print("Não é possível efetuar o saque, pois atingiu o limite do saque")
                break
            elif self.saldo < valor_saque:
                print("Você não tem saldo para realizar o saque.\nPor favor, efetue mais depósitos")
            elif valor_saque <= 0:
                print("Valor não permitido.")
                
    def extrato(self):
        print ("**************** EXTRATO ****************")
        print("Não há lançamentos de Depósito." if self.historico_deposito == "" else self.historico_deposito)
        print("Não há lançamentos de Saque." if self.historico_saque =="" else self.historico_saque)
            
        print(f"Seu saldo atual é de R$ {self.saldo}")
        print("*****************************************")
        