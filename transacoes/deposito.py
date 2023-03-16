




def deposito(self):

        while True:
            valor_deposito = float(input("Insere o valor que deseja depositar:\n"))
            if valor_deposito > 0:
                self.saldo += valor_deposito
                agora = datetime.now().strftime('%d/%m/%Y %H:%M')
                self.historico_deposito += f"Depósito em {agora} - Valor R$ {valor_deposito:.2f}\n"
                print(F"Deposito no valor de {valor_deposito} feito com sucesso.\n")
                continuar = str(input("Deseja realizar mais um deposito? \n S ou N?")).upper()
                
                if continuar == "S":
                    continue
                elif continuar == "N":
                    break   
            else:
                print("Valor não permitido.")
        return self.saldo