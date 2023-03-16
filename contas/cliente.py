import openpyxl
import pandas as pd
from pathlib import Path

ARQUIVO_CLIENTES = Path() / "contas" / "dados" / "clientes.xlsx"


class usuario(object):
    def __init__(self, CPF: str):
        self.CPF = CPF

    
    def __str__(self):
        return print(f"Dados do usuário:\
            CPF: {self.CPF}")
    
    def __doc__(self):
        pass
        
    def verficar_cadastro(self):

        f = openpyxl.load_workbook(ARQUIVO_CLIENTES)
        aba = f.active
        
        for i in range(1, len(aba['C']) + 1):
            
            if self.CPF == aba[f'C{i}'].value:
                resultado = True
                break
            else:
                resultado = False
        return resultado
            
    def adicionar_usuario(self):
        
        nome = str(input("Digita o seu nome completo:\n "))
        data_nascimento = str(input("Digita a sua data de Nascimento:\n "))
        endereçoRua = str(input("Vamos cadastrar o seu endereço:\nDigita o nome da sua rua/av:\n"))
        endereçoNumero = str(input("Digita o nome número do seu endereço:\n"))
        endereçoBairro = str(input("Digita o bairro :\n"))
        endereçoCidade = str(input("Digita o nome da cidade/Estado:\n"))
        dados = [self.CPF, nome, data_nascimento, 
                          f"Endereço: {endereçoRua}, {endereçoNumero} - bairro: {endereçoBairro} - {endereçoCidade}"]
        
        verif = self.verficar_cadastro()
    
        if verif == False:
            f = openpyxl.load_workbook(ARQUIVO_CLIENTES)
            aba = f.active
            line = len(aba['A']) + 1
            id_cadastro = aba.cell(row = line, column = 1).value = int(line - 1) #criado um ID para o cliente
            status_cadastro = aba.cell(row = line, column = 2).value = "Ativado" # colocando o Status do usuário de "Ativado"
            
            for i in range(len(dados)): #inserir os dados na mesma linha
                aba.cell(row = line, column = 3+i).value = dados[i]
            f.save(ARQUIVO_CLIENTES)
            print(f"Cadastro realizado com Sucesso!\nID cliente n° {id_cadastro}, com o status de {status_cadastro}.")

        else:
            print(f"O CPF {self.CPF} já está cadastrado. Realize o cadastro de um novo CPF")
            
    def desativar_usuario(self):
        
        f = openpyxl.load_workbook(ARQUIVO_CLIENTES)
        aba = f.active
            
        for i in range(1, len(aba['C']) + 1):
            if self.CPF == aba[f'C{i}'].value:
                id_cadastro = aba[f'A{i}'].value
                status_cadastro = aba[f'B{i}'].value
                if status_cadastro != "Desativado":
                    aba.cell(row = i, column = 2).value = "Desativado"
                    print(f"O cadastro com o ID cliente n° {id_cadastro}, foi desativado com sucesso!")
                    f.save(ARQUIVO_CLIENTES)
                    break
                elif status_cadastro == "Desativado":
                    print("Cadastro já encontra-se desativado!")
                    
    def _informa_ID(self):
        f = openpyxl.load_workbook(ARQUIVO_CLIENTES)
        aba = f.active
        
        for i in range(1, len(aba['C']) + 1):
            
            if self.CPF == aba[f'C{i}'].value:
                id_cadastro = aba[f'A{i}'].value

                break
        return id_cadastro
    
    def _informa_Status(self):
        f = openpyxl.load_workbook(ARQUIVO_CLIENTES)
        aba = f.active
        
        for i in range(1, len(aba['C']) + 1):
            
            if self.CPF == aba[f'C{i}'].value:
                status_cadastro = aba[f'B{i}'].value
                resultado = status_cadastro
                break
        return resultado

    
    def ativar_usuario(self):
        
        f = openpyxl.load_workbook(ARQUIVO_CLIENTES)
        aba = f.active
    
        for i in range(1, len(aba['C']) + 1):

            if self.CPF == aba[f'C{i}'].value:  
                id_cadastro = aba[f'A{i}'].value
                status_cadastro = aba[f'B{i}'].value
       
                if status_cadastro == "Desativado":
                    aba.cell(row = i, column = 2).value = "Ativado"
                    f.save(ARQUIVO_CLIENTES)
                    print(f"O cadastro com o ID cliente n° {id_cadastro}, foi Ativado com sucesso!")
                    break
                elif status_cadastro == "Ativado":
                    print("Cadastro já encontra-se desativado!")
                    
def listar_usuarios():
    f = pd.read_excel(ARQUIVO_CLIENTES)
    print(f)
      