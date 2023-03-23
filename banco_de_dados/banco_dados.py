from pathlib import Path
import sys
sys.path.append(str(Path().absolute()))

#temporariamente estou usando esses "banco de dados", que são 2 planilhas ... k k k k k k k k 
arquivo_clientes = Path().absolute() / "banco_de_dados" / "clientes.xlsx"
arquivo_contas = Path().absolute()  / "banco_de_dados" / "contas.xlsx"

from banco_de_dados import config as BD
import mysql.connector


meuDB = mysql.connector.connect(
    host=BD.endereço_host,
    user=BD.usuario,
    password=BD.senha,
    database=BD.meu_banco_dados
)

mycursor = meuDB.cursor()

class Tabela:

    def mostrar_tabelas():
        
        # Exemplos:
        #mycursor.execute("SHOW TABLES*")
        mycursor.execute("SHOW TABLES")
        for m in mycursor:
            print(m)
            
    def remover_tabela(tabela):
        
        # Exemplos:
        #mycursor.execute(f"DROP TABLE {tabela}")
        mycursor.execute(f"DROP TABLE {tabela}")
        
    #remover_tabela("clientes")
    def alterar_tabela():

        #Aqui terá várias funções atreladas onde poderei fazer várias coisas para alterar algo da tabela.

        # Exemplos:
        #mycursor.execute("ALTER TABLE cnaes ADD COLUMN cnaes_id INT AUTO_INCREMENT PRIMARY KEY")
        #mycursor.execute(f"ALTER TABLE {tabela} ADD COLUMN {coluna} {tipo}({tamanho}))")
        #mycursor.execute("ALTER TABLE contas ADD CONSTRAINT fk_conta_cliente FOREIGN KEY (id_user) REFERENCES clientes(id)")
        #mycursor.execute(f"ALTER TABLE contas ADD CONSTRAINT fk_conta_cliente FOREIGN KEY id REFERENCES clientes(id)")

        mycursor.execute("ALTER TABLE contas ADD CONSTRAINT fk_conta_tipo_conta FOREIGN KEY (id_tipo_conta) REFERENCES tipo_contas(id)")

    def criar_tabelas():
        
        # Exemplos:
        # mycursor.execute("CREATE TABLE socios (name VARCHAR(255))")
        # mycursor.execute("CREATE TABLE cnaes (name VARCHAR(255), address VARCHAR(255))")
        mycursor.execute("CREATE TABLE clientes (id INT AUTO_INCREMENT PRIMARY KEY, \
                        status BIT NOT NULL,\
                        cpf VARCHAR(255) NOT NULL, \
                        nome VARCHAR(255), \
                        data_nascimento VARCHAR(255),\
                        endereco VARCHAR(255),\
                        email VARCHAR(255),\
                        telefone VARCHAR(255),\
                        senha VARCHAR(255))")
        print(f"Tabela clientes criada com sucesso!")


        mycursor.execute("CREATE TABLE contas (conta INT AUTO_INCREMENT PRIMARY KEY, \
                        agencia VARCHAR(4),\
                        status BIT NOT NULL,\
                        id_user INT NOT NULL,\
                        id_tipo_conta INT, \
                        senha VARCHAR(255))")
        
        print(f"Tabela contas criada com sucesso!")

        mycursor.execute("CREATE TABLE tipo_contas (id INT AUTO_INCREMENT PRIMARY KEY,\
                        descrição VARCHAR(20),\
                        limite_valor_saque INT(4),\
                        limite_qtd_saque_mensal INT(2),\
                        limite_qtd_saque_diario INT(1))")
        
        print(f"Tabela tipo_contas criada com sucesso!")

        #mycursor.execute(f"ALTER TABLE contas ADD CONSTRAINT fk_conta_cliente FOREIGN KEY id REFERENCES clientes(id)")
        #mycursor.execute(f"CREATE TABLE {tabela} ({colunas} {tipo}({tamanho}))")


# Tabela.criar_tabelas()
# Tabela.alterar_tabela()
# Tabela.mostrar_tabelas()


def mostrar_bancos_de_dados():
    mycursor.execute("SHOW DATABASES")
    for m in mycursor:
        print(m)


class Procurar:
    def __init__(self, CPF):
        self.CPF = str(CPF)
    def cpf(self):

        try:
            mycursor.execute(f"SELECT id FROM clientes WHERE cpf ='{self.CPF}'")
            mycursor.fetchone()[0]
            return True # Será verdadeiro se o CPF existir no banco de dados.
        except:
            return False # Será false se o CPF não existir no banco de dados.

    def procurar_conta(self):
        pass
    

    def procurar_id(self):
        try:
            mycursor.execute(f"SELECT id FROM clientes WHERE cpf={self.CPF}")
            id = mycursor.fetchone()[0]
            return id# Será verdadeiro se o CPF existir no banco de dados.
        except:
            return "Error" # Será false se o CPF não existir no banco de dados.
    
    def procurar_status(self):
        try:
            mycursor.execute(f"SELECT status FROM clientes WHERE cpf={self.CPF}")
            id = mycursor.fetchone()[0]
            if id == 1: # Será verdadeiro se no BD está "true"
                return "Ativado"
            elif id == 0: # Será false se no BD está "false"
                return "Desativado"
        except:
            return "Error" # Será false se o CPF não existir no banco de dados.
    
    def procurar_senha(self):
        pass
        

class Inserir:
    
    def dados_cliente(CPF:str, 
                        nome:str=None, 
                        data_nascimento:str=None, 
                        endereco:str=None, 
                        email:str=None, 
                        telefone:str=None, 
                        senha:str=None ):
        dados = ""
        if nome != None:
            dados += f" , '{nome}'"
        if data_nascimento != None:
            dados += f" , '{data_nascimento}'"
        if endereco != None:
            dados +=f" , '{endereco}'"
        if email != None:
            dados += f" , '{email}'"
        if telefone != None:
            dados += f" , '{telefone}'"
        if senha != None:
            dados += f" , '{senha}'"
                    
        resultado = Procurar(CPF).cpf()
        
        print(dados)
        if resultado:
            print(f"O CPF informado já encontra-se cadastrado.")
            resultado = False
        else:
            try: 
                mycursor.execute(f"INSERT INTO clientes(status, cpf, nome, data_nascimento, \
                endereco, email, telefone, senha)\
                VALUES(1, '{CPF}' {dados})")
                # Ao inserir um novo cadastro, o usuário já vem "Ativado" por padrão.
                # id = mycursor.fetchall()
                meuDB.commit()
                resultado = True
            except mysql.connector.Error as error:
                print("Falha na inserção dos dados!: {}".format(error))
                meuDB.rollback()
                resultado = False

        return resultado
    
    def dados_conta():
        pass
    
class Atualizar:
    
    def dados_cliente(CPF:str, 
                nome:str=None, 
                data_nascimento:str=None, 
                enderecoRua:str=None, 
                enderecoNumero:str=None,
                enderecoBairro:str=None,
                enderecoCidade:str=None,
                enderecoEstado:str=None,
                email:str=None, 
                telefone:str=None, 
                senha:str=None ):
        
        dados = ""
        if nome != None:
            dados += f"nome='{nome}', "
        if data_nascimento != None:
            dados += f"data_nascimento='{data_nascimento}', "
        if enderecoRua != None:
            dados +=f"enderecoRua='{enderecoRua}', "
        if enderecoBairro != None:
            dados +=f"enderecoBairro='{enderecoBairro}', "
        if enderecoCidade != None:
            dados +=f"enderecoCidade='{enderecoCidade}', "
        if enderecoEstado != None:
            dados +=f"enderecoEstado='{enderecoEstado}', "
        if email != None:
            dados += f"email='{email}', "
        if telefone != None:
            dados += f"telefone='{telefone}', "
        if senha != None:
            dados += f"senha='{senha}', "
        
        dados = dados[:-2]
         
        try: 
            mycursor.execute(f"UPDATE clientes\
            SET {dados}\
            WHERE cpf='{CPF}'")
            
            meuDB.commit()
        except mysql.connector.Error as error:
            print("Database Update Failed !: {}".format(error))
            meuDB.rollback()
            


    def dados_conta(conta):
        pass


# Atualizar.dados_cliente("01912841223", 
#                         senha="123456", 
#                         endereco="R. Escorpião, 11700. Bairro: Ulisses Guimarães. Porto Velho/RO", 
#                         email="alefsander@alefsander.dev", 
#                         telefone="(69)99645-1333", 
#                         nome="Alefsander Ribeiro Nascimento")



#resultado = procurarcpf("0000000000")
#print(resultado)


def selecionar_tabela():
    CPF = '01912841223'
    mycursor.execute(f"SELECT id FROM clientes WHERE cpf={CPF}")

    print(mycursor.fetchall())
    
#selecionar_tabela()
#resposta = Inserir.dados_cliente("04240084245")
#print(resposta)


