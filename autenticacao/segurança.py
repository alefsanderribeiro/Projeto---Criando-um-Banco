from pathlib import Path
import sys
sys.path.append(str(Path().absolute()))
import openpyxl
from banco_de_dados.banco_dados import arquivo_contas
import argon2


argon2Hasher = argon2.PasswordHasher(
    time_cost=3, # número de interações 
    memory_cost=256 * 1024, # 256mb
    parallelism=1, # how many parallel threads to use
    hash_len=64, # the size of the derived key
    salt_len=32, # the size of the random generated salt in bytes
    encoding='utf-8'
)


password = b'1612772310'
 
hash = argon2Hasher.hash(password)

print(hash)
password2 = "1612772310"
try:
    verifyValid = argon2Hasher.verify(hash, password2)
    print("Senha correta")
except:
    print("Senha inválida")



class Senha:
    
    def __init__(self, numero_conta):
        self.numero_conta = numero_conta
    

    def _verificar_senha(self):
        
        senha_atual = str(input("Digita a sua senha..."))
        # senha = senha_atual.encode('utf-8')
        self.numero_conta = int(self.numero_conta)
        f = openpyxl.load_workbook(arquivo_contas)
        aba = f.active
        for i in range(1, len(aba['A']) + 1):
            if self.numero_conta == aba[f'A{i}'].value:
                try:
                    resultado = argon2Hasher.verify(aba[f'H{i}'].value, senha_atual)
                    print("Senha correta")
                    break
                except:
                    resultado = False
                    print("Senha correta")

        return resultado

    def _inserir_senha_nova(self, nova_senha):
        hash = argon2Hasher.hash(nova_senha)
        f = openpyxl.load_workbook(arquivo_contas)
        aba = f.active

        for i in range(1, len(aba['A']) + 1):
            if self.numero_conta == aba[f'A{i}'].value:
                senha_nova = aba.cell(row = i, column = 8).value = hash
                print("Foi gravado a nova senha")
                f.save(arquivo_contas)
                break

    def _nova_senha(self):
        while True:
            nova_senha1 = str(input("Digita a nova senha."))
            nova_senha2 = str(input("Digita novamente a nova senha."))
            
            if nova_senha1 == nova_senha2:
                resultado = self._inserir_senha_nova(nova_senha1)
                break
            else:
                print("As senhas apresentada não são identicas, digite novamente!")
        return nova_senha1

    def alterar_senha(self):

        while True:
            
            senha = self._verificar_senha()
            if senha == True:
                self._nova_senha()
                print("Senha alterada com sucesso!")
                break

            else:
                print("Senha errada, digita novamente!")
                














