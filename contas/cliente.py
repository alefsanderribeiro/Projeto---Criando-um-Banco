from pathlib import Path
import sys
sys.path.append(str(Path().absolute()))
import autenticacao.autenticacao_conta  as aut_conta
import autenticacao.autenticacao_senha  as aut_senha
from autenticacao.criptografia  import Crypt
import banco_de_dados as bd
import logs


class Cliente:

    def __init__(self, CPF: str):

        self.CPF = CPF
                    
    def __str__(self):
        return self.CPF
    
    def __doc__(self):
        pass
    
    
    def adicionar_endereço_usuário(self):
        endereço = {'CEP': str(input("Digita o CEP:\n")),
        'logradouro': str(input("Digita o logradouro:\n")),
        'número': str(input("Digita o nome número do seu endereço:\n")),
        'complemento': str(input("Digita o complemento:\n")),
        'bairro': str(input("Digita o nome do bairro:\n")),
        'cidade': str(input("Digita o nome da cidade :\n")),
        'estado': str(input("Digita o nome do Estado :\n"))}
        
        logs.logging.info(endereço)
        
        resultado = bd.Inserir.endereço(self.CPF, endereço['CEP'], 
                                        endereço['logradouro'], 
                                        endereço['número'], 
                                        endereço['complemento'], 
                                        endereço['bairro'], 
                                        endereço['cidade'], 
                                        endereço['estado'])

        if resultado:
            logs.logging.info("Endereço inserido com sucesso!")
            print(f"Cadastro realizado com Sucesso!")
        else:
            logs.logging.error("Não foi possível inserior o endereço!")
            print("Não foi possível inserir o endereço!")
    
    def adicionar_usuario(self):
        
        logs.logging.info("Antes de realizar o cadastro, vamos verificar se o CPF informado \
            já está cadastrado")
        verif = bd.Procurar.cpf(self.CPF)
        logs.logging.info(f"A verificação do CPF teve um resultado de: {verif}")
        
        if verif:
            logs.logging.info(f"O CPF número {self.CPF} já está cadastrado.")
            print(f"O CPF {self.CPF} já está cadastrado. Realize o cadastro de um novo CPF")
        
        else:
            
            logs.logging.info(f"O CPF número {self.CPF} NÃO está cadastrado. \
                Vamos começar o processo de cadastro de um novo usuário.")

            dados_pessoais = {'nome': str(input("Digita o seu nome completo:\n ")),
                            'rg': str(input("Digita o seu RG (Registro Geral):\n ")),
                            'orgão_RG': str(input("Digita o Orgão Expedidor do RG / Estado:\n ")),
                            'data_emissão_RG': str(input("Digita a data de emimssão do RG:\n ")),
                            'data_nascimento': str(input("Digita a sua data de Nascimento:\n ")),
                            'sexo': str(input("Digita o sexo:\n")),
                            'nacionalidade': str(input("Qual o Pais que você nasceu?\n")),
                            'naturalidade': str(input("Qual cidade/estado que você nasceu?\n")),
                            'nome_pai': str(input("Digita o nome completo do seu pai:\n")),
                            'nome_mae': str(input("Digita o nome completo da sua mãe:\n"))
                            }

            logs.logging.info(dados_pessoais)
            
            resultado = bd.Inserir.dados_cliente_pf(self.CPF,
                                                    nome=dados_pessoais['nome'],
                                                    rg=dados_pessoais['rg'],
                                                    orgão_RG=dados_pessoais['orgão_RG'],
                                                    data_emissão_RG=dados_pessoais['data_emissão_RG'],
                                                    data_nascimento=dados_pessoais['data_nascimento'],
                                                    sexo=dados_pessoais['sexo'],
                                                    nacionalidade=dados_pessoais['nacionalidade'],
                                                    naturalidade=dados_pessoais['naturalidade'],
                                                    nome_pai=dados_pessoais['nome_pai'],
                                                    nome_mae=dados_pessoais['nome_mae']) 
             
            logs.logging.info(f"O Resultado de inserção dos dados é: {resultado}")
            #senha = aut_senha.Senha(self.CPF)._nova_senha(conta_ou_usuario="usuario")
            
            if resultado:
                logs.logging.info("Cadastro feito com sucesso!")
                print(f"Cadastro realizado com Sucesso!")
                
                
                while True:
                    opcao = str(input("Deseja cadastrar um novo endereço? 'S' ou 'N' ?.")).upper()
                    
                    if opcao == "S":
                        self.adicionar_endereço_usuário()
                        continue
                        
                    elif opcao == "N":
                        break 
                    else:
                        print("Operação Inválida, por favor selecione novamente a operação desejada.")
                        
                while True:
                    opcao = str(input("Deseja cadastrar um número para contato? 'S' ou 'N' ?.")).upper()
                    
                    if opcao == "S":
                        
                        telefone = str(input("Digita o seu telefone pessoal:\n"))
                        email = str(input("Digita o seu email pessoal:\n"))
                        #bd.Inserir._telefone(Procurar.id_pf(CPF))

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


