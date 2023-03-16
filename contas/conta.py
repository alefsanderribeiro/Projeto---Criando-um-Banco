# Nesse arquivo ficará todas as funções bancárias e configurações do banco
from pathlib import Path
import sys
sys.path.append(str(Path().absolute()))
from datetime import datetime
import openpyxl
import pandas as pd

from .cliente import Cliente
# from configuracoes.banco_dados import arquivo_cliente
# banco_dados.arquivo_cliente()

import banco_de_dados.banco_dados as bd
import autenticacao.segurança as seg

class Conta:
    
    def __init__(self):
        self.agencia = "0001"
        self.conta = "conta"
        self.saldo = "saldo"
        self.qtd_saque = "quantidade_saque_efetuado"
        self.historico_deposito = "historico_deposito"
        self.historico_saque = "historico_saque"
        self.LIMITE = {"Valor_Saque": 500, "Qtd_Saque": 3}
        self.LIMITE_VALOR_SAQUE = 500
        self.LIMITE_QUANT_SAQUE = 3
        
    def _LIMITES_CONTA(self):
        pass
        
    def _aumentar_limite(self):
        pass
    
    
    def _diminuir_limite(self):
        pass        
        
    def criar_conta(self, CPF):
        ID = Cliente(CPF)._informa_ID()
        status = Cliente(CPF)._informa_Status()
        
        if status == "Desativado":
            resultado = "O usuário está desativado!"
        elif status == "Ativado":
            
            f = openpyxl.load_workbook(bd.arquivo_contas)
            aba = f.active
    
            tipo_conta = self._tipo_conta()

            line = len(aba['A']) + 1
            numero_conta = aba.cell(row = line, column = 1).value = int(line - 1) # criado o número da conta
            agencia = aba.cell(row = line, column = 2).value = self.agencia # inserindo o número da agencia
            id_usuario = aba.cell(row = line, column = 3).value = ID
            t_conta = aba.cell(row = line, column = 4).value = tipo_conta # inserindo o Tipo de Conta no cadastro.
            status_conta = aba.cell(row = line, column = 5).value = "Ativado" # inserindo o Status de Conta no cadastro.
            limite_valor_saque = aba.cell(row = line, column = 6).value = self.LIMITE_VALOR_SAQUE # inserindo o valor limite do saque.
            limite_quant_saque = aba.cell(row = line, column = 7).value = self.LIMITE_QUANT_SAQUE # inserindo a quantidade do saque diário.
            f.save(bd.arquivo_contas)
            senha = seg.Senha(numero_conta)._nova_senha()
            
            resultado = f"""Cadastro realizado com Sucesso!
                            Conta n°: {numero_conta}
                            Agência n°: {agencia}
                            CPF usuário n°: {CPF} (ID: {id_usuario})
                            Tipo de Conta: {t_conta}
                            Status da Conta: {status_conta}
                            Valor Limite por Saque: {limite_valor_saque}
                            Limite da Quantidade deSaque: {limite_quant_saque}
                            senha: {senha}
                            """
        return resultado




    def excluir_conta(self):
        pass
    
    
    
    def ativar_conta(self):
        pass
    
    
    
    def desativar_conta(self):
        pass
    
    
    
    def _tipo_conta(self):
        
        tipo_conta = ""
        
        while True:
            tipo_conta = str(input("""Informa o tipo de conta:
                                    'CC' = Conta Corrente
                                    'CP' = Conta Poupança
                                    'CS' = Conta Salário\n
                                    """)).upper()
        
            if tipo_conta == "CC":
                resultado = "CC"
                break

            elif tipo_conta == "CP":
                resultado = "CP"
                break

            elif tipo_conta == "CS":
                resultado = "CS"
                break
            else:
                print("Opção incorreta, insere novamente o Tipo de Conta!")
        return resultado
    
    def transferir_mesmo_banco(self):
        pass
    
    
        
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
                

        




        