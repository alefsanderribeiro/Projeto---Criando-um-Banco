from pathlib import Path
import sys
sys.path.append(str(Path().absolute()))
import openpyxl
import contas.cliente as cliente
from banco_de_dados import banco_dados as bd


# Todas as funções nesse arquivo são referentes a autenticação do usuário.
# 
# Onde há verifica de Cadastro do CPF, verificação da Conta e verificação das Contas no CPF cadastrado.
class Verificacao:
    def __init__(self):
        pass
        
    def cadastro(self, CPF):
        resposta = bd.Procurar(CPF).cpf()
        return resposta
    

    def _CONTA(self, CONTA):
        pass
        return contas
        
    def _contas_no_CPF(self, CPF):
        pass
        return contas

    def contas(self, cpf_or_conta):
        
        if 1 <= len(cpf_or_conta) <= 10:
            print(self._CONTA(cpf_or_conta))
            
        elif len(cpf_or_conta) == 11:
            print(self._contas_no_CPF(cpf_or_conta) )
                
        #return resultado
        
