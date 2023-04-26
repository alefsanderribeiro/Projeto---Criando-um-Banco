from pathlib import Path
import sys
sys.path.append(str(Path().absolute()))
import autenticacao.autenticacao_conta  as aut_conta
import autenticacao.autenticacao_senha  as aut_senha
from autenticacao.criptografia  import Crypt
import banco_de_dados.banco_dados as bd


class Cliente:

    def __init__(self, CPF: str):

        self.CPF = CPF
                    
    def __str__(self):
        return self.CPF
    
    def __doc__(self):
        pass
    

    def adicionar_usuario(self):
        
        print("Deu certo iniciar o cadastro")
        verif = bd.Procurar(self.CPF).cpf()
        if verif:
            print(f"O CPF {self.CPF} já está cadastrado. Realize o cadastro de um novo CPF")
        
        else:
        
            nome = str(input("Digita o seu nome completo:\n "))
            data_nascimento = str(input("Digita a sua data de Nascimento:\n "))
            endereçoRua = str(input("Vamos cadastrar o seu endereço:\nDigita o nome da sua rua/av:\n"))
            endereçoNumero = str(input("Digita o nome número do seu endereço:\n"))
            endereçoBairro = str(input("Digita o bairro:\n"))
            telefone = str(input("Digita o seu telefone pessoal:\n"))
            email = str(input("Digita o seu email pessoal:\n"))
            # dados_completo = [nome, data_nascimento, 
            #         f"{endereçoRua}, {endereçoNumero} - bairro: {endereçoBairro} - {endereçoCidade}", 
            #         telefone, email]
            
            senha = aut_senha.Senha(self.CPF)._nova_senha(conta_ou_usuario="usuario")

            resultado = bd.Inserir.dados_cliente(self.CPF, 
                                                nome=nome, 
                                                data_nascimento=data_nascimento, 
                                                enderecoRua=endereçoRua,
                                                enderecoNumero=endereçoNumero,
                                                enderecoBairro=endereçoBairro,
                                                telefone=telefone, 
                                                email=email, 
                                                senha=senha)
            
            if resultado:
                print(f"Cadastro realizado com Sucesso!")
            else:
                print("Não foi possível cadastrar o usuário!")

    
    def procuar_status(self):
        status = bd.Procurar(self.CPF).procurar_status()
        return status

    def alterar_status(self, ativado_ou_desativado="Ativado" or "Desativado"):
        
        if ativado_ou_desativado == "Ativado":
            bd.Atualizar().dados_cliente(self.CPF, status=1)
        elif ativado_ou_desativado == "Desativado":
            bd.Atualizar().dados_cliente(self.CPF, status=0)
        else:
            raise ValueError

    def informa_ID(self):
        id_cadastro = bd.Procurar(self.CPF).id()
        return id_cadastro

