from pathlib import Path
import sys
sys.path.append(str(Path().absolute()))
import openpyxl
import contas.cliente as cliente
from banco_de_dados import banco_dados as bd
from autenticacao.criptografia import Crypt


# Todas as funções nesse arquivo são referentes a autenticação do usuário.
# 
# Onde há verifica de Cadastro do CPF, verificação da Conta e verificação das Contas no CPF cadastrado.
class Verificacao:
    def __init__(self):
        pass
        
    def cadastro(self, CPF):
        CPF = Crypt().crypt(CPF)
        resultado = bd.Procurar(CPF).cpf()
        return resultado
    

    def _CONTA(self, CONTA):
        
        CONTA = int(CONTA)
        f = openpyxl.load_workbook(arquivo_contas)
        aba = f.active
        contas = ""

        for i in range(1, len(aba['A']) + 1):
            
            if CONTA == aba[f'A{i}'].value:
                agencia = aba[f'B{i}'].value
                conta = aba[f'A{i}'].value
                tipo_conta = aba[f'D{i}'].value
                status_conta = aba[f'E{i}'].value
                dados = f"Agencia: {agencia} - \
                Conta: {conta} - \
                Tipo de Conta: {tipo_conta} - \
                Status da Conta: {status_conta}\n"
                contas += dados
                
            else:
                pass
        return contas
        
    def _contas_no_CPF(self, CPF):
        
        f = openpyxl.load_workbook(arquivo_contas)
        aba = f.active
        ID = cliente.Cliente(CPF)._informa_ID()
        contas = ""

        for i in range(1, len(aba['A']) + 1):
            
            if ID == aba[f'C{i}'].value:
                agencia = aba[f'B{i}'].value
                conta = aba[f'A{i}'].value
                tipo_conta = aba[f'D{i}'].value
                status_conta = aba[f'E{i}'].value
                dados = f"Agencia: {agencia} - Conta: {conta} - Tipo de Conta: {tipo_conta} - Status da Conta: {status_conta}\n"
                contas += dados
            else:
                pass
        return contas

    def contas(self, cpf_or_conta):
        
        if 1 <= len(cpf_or_conta) <= 10:
            print(self._CONTA(cpf_or_conta))
            
        elif len(cpf_or_conta) == 11:
            print(self._contas_no_CPF(cpf_or_conta) )
                
        #return resultado
        
