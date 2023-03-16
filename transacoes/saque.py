




def saque(self):
        while True:
            valor_saque = float(input("Insere o valor que deseja sacar:\n"))
            if 0 < valor_saque <= self.LIMITE["Valor_Saque"] and self.qtd_saque < self.LIMITE["Qtd_Saque"]\
                and valor_saque <= self.saldo:
                self.saldo -= valor_saque
                agora = datetime.now().strftime('%d/%m/%Y %H:%M')
                self.historico_saque += f"Saque em {agora} - Valor R$ {valor_saque:.2f}\n"
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