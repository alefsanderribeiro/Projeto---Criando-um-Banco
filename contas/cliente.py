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
        verif = bd.Procurar().cpf(self.CPF)
        if verif:
            print(f"O CPF {self.CPF} já está cadastrado. Realize o cadastro de um novo CPF")
        
        else:
        
            nome = str(input("Digita o seu nome completo:\n "))
            rg = str(input("Digita o seu RG (Registro Geral):\n "))
            orgão_RG = str(input("Digita o seu RG:\n "))
            data_emissão_RG = str(input("Digita a data de emimssão do RG:\n "))
            data_nascimento = str(input("Digita a sua data de Nascimento:\n "))
            sexo = str(input("Digita o seu email pessoal:\n"))
            nacionalidade = str(input("Qual o Pais que você nasceu?\n"))
            naturalidade = str(input("Em qual cidade/Estado?\n"))
            nome_pai = str(input("Digita o nome completo do seu pai:\n"))
            nome_mae = str(input("Digita o nome completo da sua mãe:\n"))
             
            senha = aut_senha.Senha(self.CPF)._nova_senha(conta_ou_usuario="usuario")

            resultado = bd.Inserir.dados_cliente_pf(self.CPF,
                                                    nome=nome,
                                                    rg=rg,
                                                    orgão_RG=orgão_RG,
                                                    data_emissão_RG=data_emissão_RG,
                                                    data_nascimento=data_nascimento,
                                                    sexo=sexo,
                                                    nacionalidade=nacionalidade,
                                                    naturalidade=naturalidade,
                                                    nome_pai=nome_pai,
                                                    nome_mae=nome_mae)    
        
            if resultado:
                print(f"Cadastro realizado com Sucesso!")
                
                
                while True:
                    opcao = str(input("Deseja cadastrar um novo endereço? 'S' ou 'N' ?.")).upper()
                    
                    if opcao == "S":
                        
                        CEP = str(input("Digita o CEP:\n"))
                        logradouro = str(input("Digita o logradouro:\n"))
                        número = str(input("Digita o nome número do seu endereço:\n"))
                        complemento = str(input("Digita o complemento:\n"))
                        bairro = str(input("Digita o nome do bairro:\n"))
                        cidade = str(input("Digita o nome da cidade :\n"))
                        estado = str(input("Digita o nome do Estado :\n"))
                        
                        bd.Inserir.endereço(bd.Inserir.endereço(self.CPF, logradouro, número, CEP, bairro, complemento, cidade, estado))

                    elif opcao == "N":
                        break 
                    else:
                        print("Operação Inválida, por favor selecione novamente a operação desejada.")
                        
                while True:
                    opcao = str(input("Deseja cadastrar um número para contato? 'S' ou 'N' ?.")).upper()
                    
                    if opcao == "S":
                        
                        telefone = str(input("Digita o seu telefone pessoal:\n"))
                        email = str(input("Digita o seu email pessoal:\n"))
                        bd.Inserir._telefone(Procurar.id_pf(CPF))

                    elif opcao == "N":
                        break
                    else:
                        print("Operação Inválida, por favor selecione novamente a operação desejada.")
                        
                        
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

