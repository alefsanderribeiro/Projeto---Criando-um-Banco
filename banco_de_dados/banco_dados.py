from pathlib import Path
import sys
sys.path.append(str(Path().absolute()))

#temporariamente estou usando esses "banco de dados", que são 2 planilhas ... k k k k k k k k 
arquivo_clientes = Path().absolute() / "banco_de_dados" / "clientes.xlsx"
arquivo_contas = Path().absolute()  / "banco_de_dados" / "contas.xlsx"

from banco_de_dados import config as BD
from autenticacao.criptografia  import Crypt
import mysql.connector


meuDB = mysql.connector.connect(
    host=BD.endereço_host,
    user=BD.usuario,
    password=BD.senha,
    database=BD.meu_banco_dados
)

mycursor = meuDB.cursor()

chave = Crypt().chave_crypto().decode()
print(chave)

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
        self.CPF = CPF
        
    def cpf(self):
        mycursor.execute(f"SELECT cpf FROM clientes WHERE AES_DECRYPT(UNHEX(cpf), ('{chave}')) = '{self.CPF}'")
        cpf = mycursor.fetchone()[0]     
        if cpf == None:
            resultado = False
            
        else:
            resultado = True
        return resultado

    def id(self):
        mycursor.execute(f"SELECT id FROM clientes WHERE AES_DECRYPT(UNHEX(cpf), ('{chave}')) = '{self.CPF}'")
        id = mycursor.fetchone()[0]     
        if id != None:
            resultado = id
        else:
            resultado = "Error"
        return resultado

    def procurar_conta(self):
        mycursor.execute(f"SELECT id, id_agencia, id_conta FROM contas WHERE AES_DECRYPT(UNHEX(id_cliente), ('{chave}')) = '{self.id}'")
        id = mycursor.fetchall()  
        if id != None:
            resultado = id
        else:
            resultado = "Error"
        return resultado
    

        # try:
        #     mycursor.execute(f"SELECT id FROM clientes WHERE cpf={self.CPF}")
        #     id = mycursor.fetchone()[0]
        #     return id# Será verdadeiro se o CPF existir no banco de dados.
        # except:
        #     return "Error" # Será false se o CPF não existir no banco de dados.
    
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
        

resultado = Procurar("01912841223").id()

print(resultado)

class Inserir:
    
    def dados_cliente(CPF:str, 
                status=1, 
                nome:str=None, 
                data_nascimento:str=None, 
                enderecoRua:str=None, 
                enderecoNumero:str=None,
                enderecoBairro:str=None,
                email:str=None, 
                telefone:str=None, 
                senha:str=None ):
        dados = ""
        coluna_dados = ""

        if nome != None:
            dados += f"HEX(AES_ENCRYPT(('{nome}'), ('{chave}'))), "
            coluna_dados += ", nome"
            
        if data_nascimento != None:
            dados += f"HEX(AES_ENCRYPT(('{data_nascimento}'), ('{chave}'))), "
            coluna_dados += ", data_nascimento"

        if enderecoRua != None:
            dados +=f"HEX(AES_ENCRYPT(('{enderecoRua}'), ('{chave}'))), "
            coluna_dados += ", enderecoRua"
            
        if enderecoNumero != None:
            dados +=f"HEX(AES_ENCRYPT(('{enderecoNumero}'), ('{chave}'))), "
            coluna_dados += ", enderecoNumero"
            
        if enderecoBairro != None:
            dados +=f"HEX(AES_ENCRYPT(('{enderecoBairro}'), ('{chave}'))), "
            coluna_dados += ", enderecoBairro"
            
        if email != None:
            dados += f"HEX(AES_ENCRYPT(('{email}'), ('{chave}'))), "
            coluna_dados += ", email"
            
        if telefone != None:
            dados += f"HEX(AES_ENCRYPT(('{telefone}'), ('{chave}'))), "
            coluna_dados += ", telefone"
            
        if senha != None:
            dados += f"HEX(AES_ENCRYPT(('{senha}'), ('{chave}'))), "
            coluna_dados += ", senha"
                     
        dados = dados[:-2]
          
        status = f"{status}"
        CPF = f"HEX(AES_ENCRYPT(('{CPF}'), ('{chave}')))"
                  
        resultado = Procurar(CPF).cpf()
        
        print(f"INSERT INTO clientes (status, cpf {coluna_dados})\
                VALUES ({status}, {CPF}, {dados})")
        
        if resultado:
            print(f"O CPF informado já encontra-se cadastrado.")
            resultado = False
        
        else:
            try: 
                
                mycursor.execute(f"INSERT INTO clientes (status, cpf {coluna_dados})\
                    VALUES ({status}, {CPF}, {dados})")
                
                # Ao inserir um novo cadastro, o usuário já vem "Ativado" por padrão.
                # id = mycursor.fetchall()
                meuDB.commit()
                resultado = True
            except mysql.connector.Error as error:
                print("Falha na inserção dos dados!: {}".format(error))
                meuDB.rollback()
                resultado = False

        return resultado
    
# Inserir.dados_cliente("04240084245", nome="Geissilaine")

    # def dados_conta():
    #     pass
    
class Atualizar:
    
    def dados_cliente(CPF:str,
                status=1,
                nome:str=None, 
                data_nascimento:str=None, 
                enderecoRua:str=None, 
                enderecoNumero:str=None,
                enderecoBairro:str=None,
                enderecoCidade:str=None,
                email:str=None, 
                telefone:str=None, 
                senha:str=None ):
        
        dados = ""
        if status == 0:
            dados += f"status='{status}', "
        if nome != None:
            dados += f"nome='{nome}', "
        if data_nascimento != None:
            dados += f"data_nascimento='{data_nascimento}', "
        if enderecoRua != None:
            dados +=f"enderecoRua='{enderecoRua}', "
        if enderecoBairro != None:
            dados +=f"enderecoNumero='{enderecoNumero}', "
        if enderecoBairro != None:
            dados +=f"enderecoBairro='{enderecoBairro}', "
        if enderecoCidade != None:
            dados +=f"enderecoCidade='{enderecoCidade}', "
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
    CPF = '04240084245'
    mycursor.execute(f"SELECT id FROM clientes WHERE cpf={CPF}")

    print(mycursor.fetchall())
    
#selecionar_tabela()
#resposta = Inserir.dados_cliente("04240084245")
#print(resposta)



    """
# Comando no SQL para criptografar e descriptografar dados salvos
    

INSERT INTO historico_transacoes (funcao_nome, log)
VALUES (HEX(AES_ENCRYPT(("01912841223"), (SELECT hash FROM chave WHERE chave.id=1))));


INSERT INTO historico_transacoes (funcao_nome, log)
VALUES (HEX(AES_ENCRYPT(("01912841223"), (SELECT hash FROM chave WHERE chave.id=1))), AES_ENCRYPT("01912841223", (SELECT hash FROM chave WHERE chave.id=1)));

INSERT INTO historico_transacoes (log)
VALUES (HEX(AES_ENCRYPT("01912841223", (SELECT hash FROM chave WHERE chave.id=1))));

SELECT AES_DECRYPT(log, (SELECT hash FROM chave WHERE chave.id=1)) FROM historico_transacoes;


/*

Essas funções são para selecionar

*/
SELECT * FROM historico_transacoes WHERE AES_DECRYPT(log, (SELECT hash FROM chave WHERE chave.id=1)) = '01912841223';

SELECT * FROM historico_transacoes WHERE AES_DECRYPT(UNHEX(funcao_nome), (SELECT hash FROM chave WHERE chave.id=1)) = '01912841223';

SELECT id FROM historico_transacoes WHERE AES_DECRYPT(UNHEX(log), (SELECT hash FROM chave WHERE chave.id=1)) = '04240084245';



    """




