from pathlib import Path
import sys
sys.path.append(str(Path().absolute()))
from cryptography.fernet import Fernet

ARQUIVO_CHAVE_CRYPTO = Path() / "autenticacao" / "chave.txt"

# Criptografar e descriptografar os dados.

class Crypt:
    def __init__(self):
        pass
    
    def __gerar_chave(self, arquivo):
        chave = Fernet.generate_key()
        with open(arquivo,"wb") as arquivo_chave:
            arquivo_chave.write(chave)
            
    def __ler_chave(self, arquivo):
        with open(arquivo,"rb") as arquivo_chave:
            chave = arquivo_chave.read()
        return chave

    def chave_crypto(self):
        try:
            chave = self.__ler_chave(ARQUIVO_CHAVE_CRYPTO)
        except FileNotFoundError:
            self.__gerar_chave(ARQUIVO_CHAVE_CRYPTO)
            chave = self.__ler_chave(ARQUIVO_CHAVE_CRYPTO)
        return chave

    def crypt(self, valor_criptografar):
        chave = self.chave_crypto()
        f = Fernet(chave)
        crypt = f.encrypt(valor_criptografar.encode())
        crypt = crypt.decode()
        return crypt
    
    def descrypt(self, valor_descriptografar):
        chave = self.chave_crypto()
        f = Fernet(chave)
        descrypt = f.decrypt(valor_descriptografar.encode())
        descrypt = descrypt.decode()

        return descrypt
    

# nome = Crypt().crypt(str(input("Digita o seu nome completo:\n ")))
# print(nome)


# nome1 = Crypt().descrypt(nome)
# print(nome1)
