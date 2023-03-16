



def extrato(self):
    print ("**************** EXTRATO ****************")
    print("Não há lançamentos de Depósito." if self.historico_deposito == "" else self.historico_deposito)
    print("Não há lançamentos de Saque." if self.historico_saque =="" else self.historico_saque)
    print(f"Seu saldo atual é de R$ {self.saldo}\n")
    agora = datetime.now().strftime('%d/%m/%Y %H:%M')
    print(f"Data: {agora}")
    print("*****************************************")