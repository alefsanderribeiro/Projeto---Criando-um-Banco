from pathlib import Path
import sys
sys.path.append(str(Path().absolute()))
import openpyxl
from autenticacao.criptografia import Crypt
import banco_de_dados as bd
import argon2
import re


argon2Hasher = argon2.PasswordHasher(
    time_cost=3, # número de interações 
    memory_cost=256 * 1024, # 256mb
    parallelism=1, # how many parallel threads to use
    hash_len=64, # the size of the derived key
    salt_len=32 # the size of the random generated salt in bytes
)

# Todas as funções dessa Classe são referentes a autenticação da senha do usuário.

class Senha: 

    def __init__(self, CPF=None, CONTA=None):
        
        if CPF != None:
            self.CPF = Crypt().crypt(CPF)
        elif CONTA != None:
            self.numero_conta = CONTA


    def _verificar_hash_senha(self):
        reHash = argon2Hasher.check_needs_rehash(hash)
        if reHash:
            #novo_para = argon2.Parameters(type, version, salt_len, hash_len, time_cost, memory_cost, parallelism)
            pass

    def _verificar_senha(self):
        
        senha_atual = str(input("Digita a sua senha..."))
        self.numero_conta = int(self.numero_conta)
        f = openpyxl.load_workbook("")
        aba = f.active
        for i in range(1, len(aba['A']) + 1):
            if self.numero_conta == aba[f'A{i}'].value:
                
                local_senha = aba[f'H{i}'].value
                descriptografado = Crypt().descrypt(local_senha)
                try:
                    resultado = argon2Hasher.verify(descriptografado, senha_atual)
                    break
                except:
                    resultado = False

        return resultado


    def _nova_senha(self, conta_ou_usuario="conta" or "usuario"):
        while True:
            
            if conta_ou_usuario == "conta":
                nova_senha1 = self._verificacao_senha_conta()
            elif conta_ou_usuario == "usuario":
                nova_senha1 = self._verificacao_senha_usuario()
            nova_senha2 = str(input("Digita novamente a nova senha."))
            
            if nova_senha1 == nova_senha2:
                hash = argon2Hasher.hash(nova_senha1) # Gerou o Hash Argon2
                resultado = Crypt().crypt(hash) # Criptografou somente o Hash
                return resultado
            else:
                print("As senhas apresentada não são identicas, digite novamente!")
                

    def alterar_senha(self, conta_ou_usuario="conta" or "usuario"):

        while True:
            senha = self._verificar_senha()
            if senha == True:
                self._nova_senha(conta_ou_usuario)
                print("Senha alterada com sucesso!")
                break

            else:
                print("Senha errada, digita novamente!")
    
    def _verificacao_senha_usuario(self):
        while True:
            
            senha = str(input("Insere sua senha..."))
            
            while True:
                
                # Verifica se a senha contém pelo menos uma letra maiúscula
                if not re.search("[A-Z]", senha):
                    print("Sua senha deve conter pelo menos uma letra maiúscula")
                    break
                # Verifica se a senha contém pelo menos uma letra minúscula
                elif not re.search("[a-z]", senha):
                    print("Sua senha deve conter pelo menos uma letra minúscula")
                    break

                # Verifica se a senha contém pelo menos um caractere especial
                elif not re.search("[\W_]", senha):
                    print("Sua senha deve conter pelo menos um caractere especial")
                    break

                # Verifica se a senha contém pelo menos um número
                elif not re.search("[0-9]", senha):
                    print("Sua senha deve conter pelo menos um número")
                    break

                # Verifica se a senha tem pelo menos 8 caracteres
                elif len(senha) < 8:
                    print("Sua senha deve ter pelo menos 8 caracteres")
                    break

                # Se a senha atender a todos os requisitos, ela é válida
                else:
                    print("Senha válida!")
                    return senha
                    break

    def _verificacao_senha_conta(self):
        while True:
            
            senha = str(input("Insere a senha da sua conta..."))
            
            while True:
                
                # Verifica se a senha contém pelo menos um número
                if not re.match("^\d+$", senha):
                    print("Sua senha deve conter somente números")
                    break

                # Verifica se a senha tem pelo menos 8 caracteres
                elif 8 > len(senha) or len(senha) > 16:
                    print("Sua senha deve ter pelo menos 8 caracteres e até 16")
                    break

                # Se a senha atender a todos os requisitos, ela é válida
                else:
                    print("Senha válida!")
                    return senha
                    break


