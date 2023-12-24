import sys
from pathlib import Path
sys.path.append(str(Path().absolute()))

from banco_de_dados import config as BD
from autenticacao.criptografia  import Crypt
import mysql.connector
import logs

meuDB = mysql.connector.connect(
    host=BD.endereço_host,
    user=BD.usuario,
    password=BD.senha,
    database=BD.meu_banco_dados
)

mycursor = meuDB.cursor()

chave = Crypt().chave_crypto().decode()


class _verificar:
    
    def _resultado(soma):
        resultado = 11 - (soma % 11)
        return resultado
        
    
    def _CPF_ou_CNPJ(CPF_ou_CNPJ):
        if len(CPF_ou_CNPJ) == 11:
            return "CPF"
        elif len(CPF_ou_CNPJ) == 14:
            return "CNPJ"
    
    
    def CPF(CPF):
        
        list = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        
        # Verificação do primeiro dígito
        soma = 0
        for i in range(9):
            soma += int(CPF[i]) * list[i]
        
        verificador1 = _verificar._resultado(soma)
       
        # Verificação do segundo dígito
        soma = 0
        for i in range(9):
            soma += ((int(CPF[i+1]))) * list[i]

        verificador2 = _verificar._resultado(soma)

        if int(CPF[9]) == verificador1 and int(CPF[10]) == verificador2:
            resultado =  True
        else:
            resultado =  False
        
        return resultado



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
        #mycursor.execute("ALTER TABLE contas ADD CONSTRAINT fk_conta_tipo_conta FOREIGN KEY (id_tipo_conta) REFERENCES tipo_contas(id)")
        pass
    def criar_tabelas():
        # Exemplos:
        # mycursor.execute("CREATE TABLE socios (name VARCHAR(255))")
        # mycursor.execute("CREATE TABLE cnaes (name VARCHAR(255), address VARCHAR(255))")
        #mycursor.execute("CREATE TABLE clientes (id INT AUTO_INCREMENT PRIMARY KEY, \
        #                status BIT NOT NULL,\
        #                cpf VARCHAR(255) NOT NULL, \
        #                nome VARCHAR(255), \
        #                data_nascimento VARCHAR(255),\
        #                endereco VARCHAR(255),\
        #                email VARCHAR(255),\
        #                telefone VARCHAR(255),\
        #                senha VARCHAR(255))")
        
        #mycursor.execute("CREATE TABLE contas (conta INT AUTO_INCREMENT PRIMARY KEY, \
        #                agencia VARCHAR(4),\
        #                status BIT NOT NULL,\
        #                id_user INT NOT NULL,\
        #                id_tipo_conta INT, \
        #                senha VARCHAR(255))")
        
        #mycursor.execute("CREATE TABLE tipo_contas (id INT AUTO_INCREMENT PRIMARY KEY,\
        #                descrição VARCHAR(20),\
        #                limite_valor_saque INT(4),\
        #                limite_qtd_saque_mensal INT(2),\
        #                limite_qtd_saque_diario INT(1))")
        
        
        #mycursor.execute(f"ALTER TABLE contas ADD CONSTRAINT fk_conta_cliente FOREIGN KEY id REFERENCES clientes(id)")
        #mycursor.execute(f"CREATE TABLE {tabela} ({colunas} {tipo}({tamanho}))")
        pass
#Tabela.criar_tabelas()
#Tabela.alterar_tabela()
#Tabela.mostrar_tabelas()

def mostrar_bancos_de_dados():
    mycursor.execute("SHOW DATABASES")
    
    logs.logging.info(f"Função: mostrar_bancos_de_dados() - Resultado:")
    for m in mycursor:
        logs.logging.info(m)
    

def últimoIdPessoa():
    mycursor.execute(f"SELECT idPessoa FROM pessoa ORDER BY idPessoa DESC limit 1")
    try:
        id = mycursor.fetchone()[0]
        
    except:
        id = 0
    logs.logging.info(f"Função: últimoIdPessoa() - Resultado: {id}")
    return id


def últimoIdBairro():
    mycursor.execute(f"SELECT id FROM bairros ORDER BY id DESC limit 1")
    try:
        id = mycursor.fetchone()[0]
        
    except:
        id = 0
    logs.logging.info(f"Função: últimoIdBairro() - Resultado: {id}")
    return id


def últimoIdCidade():
    mycursor.execute(f"SELECT id FROM cidade ORDER BY id DESC limit 1")
    try:
        id = mycursor.fetchone()[0]
        
    except:
        id = 0
    logs.logging.info(f"Função: últimoIdCidade() - Resultado: {id}")
    return id


def últimoIdEndereço():
    mycursor.execute(f"SELECT idEndereço FROM endereço ORDER BY idEndereço DESC limit 1")
    try:
        id = mycursor.fetchone()[0]
        
    except:
        id = 0
    logs.logging.info(f"Função: últimoIdEndereço() - Resultado: {id}")    
    return id


def últimoIdUser_Funcionario():
    mycursor.execute(f"SELECT id FROM `user_sistema` ORDER BY idEndereço DESC limit 1")
    try:
        id = mycursor.fetchone()[0]
        
    except:
        id = 0
    logs.logging.info(f"Função: últimoIdEndereço() - Resultado: {id}")    
    return id


class Procurar:
    
    # Retorna se existe ou não o CPF informado
    def cpf(Número_do_CPF):
        mycursor.execute(f"SELECT CPF FROM `cliente_pf_view` WHERE AES_DECRYPT(UNHEX(CPF), ('{chave}')) = {Número_do_CPF}")
        cpf = mycursor.fetchone()
        if cpf == None:
            resultado = False
            
        else:
            resultado = True
        logs.logging.info(f"Função: Procurar.cpf() - Resultado: {resultado}") 
        return resultado
    
    # Retorna se existe ou não o CNPJ informado
    def cnpj(Número_do_CNPJ):
        mycursor.execute(f"SELECT CNPJ FROM `pessoa jurídica` WHERE AES_DECRYPT(UNHEX(CPF), ('{chave}')) = {Número_do_CNPJ}")
        cnpj = mycursor.fetchone()
        if cnpj == None:
            resultado = False
            
        else:
            resultado = True
        logs.logging.info(f"Função: Procurar.cnpj() - Resultado: {resultado}") 
        return resultado

    
    #retorna o ID do cadastro do CPF
    def _id_pf(Número_do_CPF):
        mycursor.execute(f"SELECT `idPessoa Física` FROM `pessoa física` WHERE AES_DECRYPT(UNHEX(CPF), ('{chave}')) = {Número_do_CPF}")
        logs.logging.info(f"Função: Procurar._id_pf() - Resultado: {mycursor.fetchone()[0]}")
        return mycursor.fetchone()[0]

    #retorna o ID do cadastro do CNPJ
    def _id_pj(Número_do_CNPJ):
        mycursor.execute(f"SELECT `idPessoa Jurídica` FROM `pessoa jurídica` WHERE AES_DECRYPT(UNHEX(CNPJ), ('{chave}')) = {Número_do_CNPJ}")
        logs.logging.info(f"Função: Procurar._id_pj() - Resultado: {mycursor.fetchone()[0]}")
        return mycursor.fetchone()[0]
    
    
    def id_pessoa(CPF_ou_CNPJ):
        resultado = _verificar._CPF_ou_CNPJ(CPF_ou_CNPJ)
        if resultado == "CPF":
            mycursor.execute(f"SELECT `idPessoa` FROM `pessoa física` WHERE AES_DECRYPT(UNHEX(CPF), ('{chave}')) = {CPF_ou_CNPJ}")
            try:
                id = mycursor.fetchone()[0]
                
            except:
                id = 0
            
        elif resultado == "CNPJ":
            mycursor.execute(f"SELECT `idPessoa` FROM `pessoa jurídica`  WHERE AES_DECRYPT(UNHEX(CNPJ), ('{chave}')) = {CPF_ou_CNPJ}")
            id = mycursor.fetchone()[0]
            
        logs.logging.info(f"Função: Procurar.id_pessoa() - Resultado: {id}")    
        return id
        

    def conta(self):
        mycursor.execute(f"SELECT id, id_agencia, id_conta FROM contas WHERE AES_DECRYPT(UNHEX(id_cliente), ('{chave}')) = '{self.id}'")
        id = mycursor.fetchall()  
        if id != None:
            resultado = id
        else:
            resultado = False
        logs.logging.info(f"Função: Procurar.conta() - Resultado: {resultado}")    
        return resultado
    

        # try:
        #     mycursor.execute(f"SELECT id FROM clientes WHERE cpf={self.CPF}")
        #     id = mycursor.fetchone()[0]
        #     return id# Será verdadeiro se o CPF existir no banco de dados.
        # except:
        #     return "Error" # Será false se o CPF não existir no banco de dados.
    
    def id_estado_pelo_nome(nome_do_estado):
        mycursor.execute(f"SELECT id FROM `estado` WHERE nome = '{nome_do_estado}'")
        try:
            id = mycursor.fetchone()[0]
            
        except:
            id = False
        logs.logging.info(f"Função: Procurar.id_estado_pelo_nome() - Resultado: {id}")     
        return id


    def _uf_estado_pelo_ID_cidade(id_cidade):
        mycursor.execute(f"SELECT `estado`.`uf` FROM `estado` INNER JOIN `cidade` ON `estado`.`id` = `cidade`.`estado_id` WHERE `cidade`.`id` = '{id_cidade}'")
         
        try:
            resultado = mycursor.fetchone()[0]
            
        except:
            resultado = "ID não encontrado."
        logs.logging.info(f"Função: Procurar._uf_estado_pelo_ID_cidade() - Resultado: {resultado}")    
        return resultado
    
    
    def cidade_pelo_id(id_cidade):
        mycursor.execute(f"SELECT nome FROM cidade WHERE id = '{id_cidade}'")
        try:
            resultado = mycursor.fetchone()[0]
            
        except:
            resultado = "ID não encontrado."
        logs.logging.info(f"Função: Procurar.cidade_pelo_id() - Resultado: {resultado}")    
        return resultado 
    
    def cidade(nome_da_cidade, id_etado):

        mycursor.execute(f"SELECT `cidade`.`id`, `cidade`.`nome` FROM `cidade` INNER JOIN `estado` ON `estado`.`id` = `cidade`.`estado_id` WHERE `cidade`.`nome` LIKE '%{nome_da_cidade}%' AND `estado`.`id` = '{id_etado}'")
                
        cidade = list(mycursor.fetchall())
        quantidade_cidade = len(cidade)
        
        if quantidade_cidade == 0: 
            #Cidade não encontrada
            resultado = False
        elif quantidade_cidade == 1:
            #Só existe 1 cidade com esse nome
            resultado = int(cidade[0][0])
        elif quantidade_cidade >= 1:
            #Existe mais de 1 cidade com o nome informado
            resultado = []
            for i in range(len(cidade)):
                resultado.append(f"ID: {cidade[i][0]} = {cidade[i][1]} / {Procurar._uf_estado_pelo_ID_cidade(cidade[i][0])}")
        logs.logging.info(f"Função: Procurar.cidade() - Resultado: {resultado}")         
        return resultado
    
    def bairro(nome_do_bairro, id_da_cidade):         
        mycursor.execute(f"SELECT `bairros`.`id`, `bairros`.`nome` FROM `bairros` INNER JOIN `cidade` ON `cidade`.`id` = `bairros`.`cidade_id` WHERE `bairros`.`nome` LIKE '%{nome_do_bairro}%' AND `cidade`.`id` = '{id_da_cidade}'")
        bairro = list(mycursor.fetchall())
        quantidade_bairro = len(bairro)
        
        if quantidade_bairro == 0: 
            #Bairro não encontrado
            resultado = False
        elif quantidade_bairro == 1:
            #Só existe 1 Bairro com esse nome e nessa cidade
            resultado = bairro[0][0]
        elif quantidade_bairro >= 1:
            #Existe mais de 1 Bairro com o nome informado
            resultado = []
            for i in range(len(quantidade_bairro)):
                resultado.append(f"ID: {bairro[i][0]} = {bairro[i][1]} - Cidade: {id_da_cidade} / {Procurar._uf_estado_pelo_ID_cidade(id_da_cidade)}")
        logs.logging.info(f"Função: Procurar.bairro() - Resultado: {resultado}")        
        return resultado

    #Preciso arrumar essa função. Pois ainda não colqouei o "status do cliente" no banco de dados
    def status_do_cliente(self):
        try:
            mycursor.execute(f"SELECT status FROM clientes WHERE cpf={self.CPF}")
            id = mycursor.fetchone()[0]
            if id == 1: # Será verdadeiro se no BD está "true"
                return "Ativado"
            elif id == 0: # Será false se no BD está "false"
                return "Desativado"
        except:
            return "Error" # Será false se o CPF não existir no banco de dados.
    
    # Preciso arrumar. Ainda não defini como será a "senha do cliente"
    def senha_do_cliente():
        pass
    
    
    def senha_do_funcionario(id_cadastro, senha):
        mycursor.execute(f"SELECT senha FROM `user_sistema` WHERE id = {id_cadastro} and AES_DECRYPT(UNHEX(senha), ('{chave}')) = '{senha}'")
        res = mycursor.fetchone()
        if res == None:
            resultado = False
            
        else:
            resultado = True
        logs.logging.info(f"Função: Procurar.senha_do_funcionario() - Resultado: {resultado}") 
        return resultado
        

 

def _gerar(dados):
    resultado = f"HEX(AES_ENCRYPT(('{dados}'), ('{chave}'))), "
    logs.logging.info(f"Função: _gerar() - Resultado: {resultado}")
    return resultado

class Inserir:
    
    
    def senha_funcionario_sistema(id_funcionário, nova_senha):
        
        senha = _gerar(nova_senha)
        mycursor.execute(f"INSERT INTO `user_sistema` (id, id_funcionario, senha)\
        VALUES ({últimoIdUser_Funcionario() + 1},{id_funcionário}, {senha})")
        

    def _cidade(cidade:str, id_estado:str):
        try: 
            id_cidade = últimoIdCidade()
            
            mycursor.execute(f"INSERT INTO cidade (id, nome, estado_id)\
            VALUES ({id_cidade + 1},'{cidade}', {id_estado})")
            
            logs.logging.info(f"INSERT INTO cidade (id, nome, estado_id)\
            VALUES ({id_cidade + 1},'{cidade}', {id_estado})")

            meuDB.commit()
            resultado = True
        except mysql.connector.Error as error:

            logs.logging.error("Falha na inserção dos dados!: {}".format(error))
            meuDB.rollback()
            resultado = False
        logs.logging.info(f"Função: Inserior._cidade() - Resultado: {resultado}")
        return resultado

    def _bairro(bairro:str, id_cidade:int):
        try: 
            mycursor.execute(f"INSERT INTO bairros (id, nome, cidade_id)\
            VALUES ({últimoIdBairro() + 1},'{bairro}', {id_cidade})") 
            
            logs.logging.info(f"INSERT INTO bairros (id, nome, cidade_id)\
            VALUES ({últimoIdBairro() + 1},'{bairro}', {id_cidade})")
            
            meuDB.commit()
            resultado = True
        except mysql.connector.Error as error:
            
            logs.logging.error("Falha na inserção dos dados!: {}".format(error))
            meuDB.rollback()
            resultado = False
        logs.logging.info(f"Função: Inserior._cidade() - Resultado: {resultado}")    
        return resultado
    
    def _telefone():
        pass
    
    
    # Arrumar a função para inserir telefone do cliente.
    def telefone(id):
        
        logs.logging.info("Cadastro do telefone realizado com sucesso")
        pass
        
    # Inserior o endereço do cliente
    def endereço(CPF_ou_CNPJ:str,
                 CEP:str, 
                 logradouro:str, 
                 número:str, 
                 complemento:str, 
                 bairro:str, 
                 cidade:str, 
                 estado:str):

        id_pessoa = Procurar.id_pessoa(CPF_ou_CNPJ)
        id_estado = Procurar.id_estado_pelo_nome(estado)
        id_do_último_Endereço = últimoIdEndereço() + 1
        if id_estado == False:
            #precisa verificar se o nome do estado está correto.
            logs.logging.info("ID do Estado não encontrado")
        else:
            
            # Esse é o Loope para a cidade.
            loop1 = True
            while loop1 == True:
                
                logs.logging.info("Procurar se a cidade está cadastrado!")
                resultadoCidade = Procurar.cidade(cidade, id_estado)
                
                if resultadoCidade == False:
                    #Cadastrar o nome da cidade
                    logs.logging.info("Cidade não cadastrada. Vamos realizar o cadastro!")
                    Inserir._cidade(cidade, id_estado)
                    
                elif type(resultadoCidade) == int:
                    
                    idCidade = resultadoCidade
                    logs.logging.info("Cidade única cadastrada!")
                    loop1 = False
                
                elif type(resultadoCidade) == list:
                    # Pedir a confirmação do ID correto
                    logs.logging.warning("Várias cidades estão cadastrada. \
                        Precisa confirmar a  cidade correta!")
                    logs.logging.info(resultadoCidade)
                    print(resultadoCidade)
                    resultado = int(input("Informa o ID da cidade correto para ser inserido:\n"))
                    idCidade = resultado
                    
            # Esse é o Loope para o bairro
            loop2 = True 
            while loop2 == True:
                
                logs.logging.info("Procurar se o bairro está cadastrado!")
                resultadoBairro = Procurar.bairro(bairro, idCidade)
                
                if resultadoBairro == False:
                    #Cadastrar o nome da cidade
                    Inserir._bairro(bairro, idCidade)
                    
                elif type(resultadoBairro) == int:
                    idBairro = resultadoBairro
                    
                    logs.logging.info("Bairro único cadastrada")
                    loop2 = False
                
                elif type(resultadoBairro) == list:
                    # Pedir a confirmação do ID correto
                    logs.logging.warning("Vários bairros estão cadastrados. \
                        Precisa confirmar o  bairro correto!")
                    logs.logging.info(resultadoBairro)
                    print(resultadoBairro)
                    resultado = int(input("Informa o ID do bairro correto para ser inserido:\n"))
                    idBairro = resultado
                
            try: 
                
                
                logs.logging.info(f"INSERT INTO endereço (idEndereço, CEP, Logradouro, Número, Complemento, bairros_id)\
                VALUES ('{id_do_último_Endereço}','{CEP}', '{logradouro}', '{número}', '{complemento}',{idBairro})")
                
                mycursor.execute(f"INSERT INTO endereço (idEndereço, CEP, Logradouro, Número, Complemento, bairros_id)\
                VALUES ('{id_do_último_Endereço}','{CEP}', '{logradouro}', '{número}', '{complemento}',{idBairro})") 

                logs.logging.info(f"INSERT INTO Endereço_da_pessoa (idEndereço, idPessoa, Observação)\
                VALUES ('{id_do_último_Endereço}','{id_pessoa}', NULL)") 
            
                mycursor.execute(f"INSERT INTO Endereço_da_pessoa (idEndereço, idPessoa, Observação)\
                VALUES ('{id_do_último_Endereço}','{id_pessoa}', NULL)")
                
                
                                
                meuDB.commit()
                resultado = True
            except mysql.connector.Error as error:
                logs.logging.error("Falha na inserção dos dados!: {}".format(error))
                meuDB.rollback()
                resultado = False
            return resultado    

    # Cadastro de Pessoa Física
    def dados_cliente_pf(CPF:str,
                    nome:str=None,
                    rg:str=None,
                    orgão_RG:str=None,
                    data_emissão_RG:str=None,
                    data_nascimento:str=None,
                    sexo:str=None,
                    nacionalidade:str=None,
                    naturalidade:str=None,
                    nome_pai:str=None,
                    nome_mae:str=None):
        
        resultadoCPF = Procurar.cpf(CPF)
        
        if resultadoCPF:
            logs.logging.error(f"Erro: o CPF informado já encontra-se cadastrado. ID número: {Procurar._id_pf(CPF)}")
            resultado = False
    
        else:
            
            lista = [nome, rg, orgão_RG, data_emissão_RG, data_nascimento, 
                    sexo, nacionalidade, naturalidade, nome_pai, nome_mae]
    
            colunas = ["Nome", "RG", "Orgão_RG","Data_Emissão_RG","Data_Nascimento",
                    "Sexo","Nacionalidade","Naturalidade","Nome_Pai","Nome_Mãe"]
            
            dados = ""
            coluna_dados = ""
            
            for i in range(10):
                if lista[i] == None:
                    continue
                else:
                    dados += _gerar(lista[i])
                    coluna_dados += f", {colunas[i]}"
                
            dados = dados[:-2]
            coluna_dados = coluna_dados[2:]
               
            try: 
                CPF_hash = _gerar(CPF)[:-2]
                idPessoa = últimoIdPessoa() + 1
                
                mycursor.execute(f"INSERT INTO pessoa (idPessoa, Tipo_Pessoa, Cliente, Funcionário)\
                VALUES ({idPessoa}, 0, 0, 0)") 
                # Tipo_Pessoa = 0 é Pessoa Física e 1 é Pessoa Jurídica
                # Cliente = 0 é False e 1 é Verdadeiro.
                # Funcionário = 0 é False e 1 é Verdadeiro.
                
                logs.logging.info(f"INSERT INTO pessoa (idPessoa, Tipo_Pessoa, Cliente, Funcionário)\
                VALUES ({idPessoa}, 0, 0, 0)") 
                
                mycursor.execute(f"INSERT INTO `pessoa física` (idPessoa, CPF, {coluna_dados})\
                VALUES ({idPessoa},{CPF_hash}, {dados})")
                
                logs.logging.info(f"INSERT INTO `pessoa física` (idPessoa, CPF, {coluna_dados})\
                VALUES ({idPessoa},{CPF_hash}, {dados})")
                
                meuDB.commit()
                resultado = True
            except mysql.connector.Error as error:
                logs.logging.error("Falha na inserção dos dados!: {}".format(error))
                meuDB.rollback()
                resultado = False
        logs.logging.info(resultado)
        return resultado


    # Cadastro de Pessoa Jurídica
    def dados_cliente_pj(CNPJ:str,
                         razao_social:str=None):

        CNPJ = f"HEX(AES_ENCRYPT(('{CNPJ}'), ('{chave}')))"
        resultado = Procurar(CNPJ).cnpj()

        if resultado:
            print(f"O CNPJ informado já encontra-se cadastrado.")
            resultado = False
    
        else:
            try: 
                
                dados = ""
                coluna_dados = ""

                if razao_social != None:
                    dados += f"HEX(AES_ENCRYPT(('{razao_social}'), ('{chave}'))), "
                    coluna_dados += ", Razão_Social"
            
                
                idPessoa = últimoIdPessoa() + 1
                
                mycursor.execute(f"INSERT INTO pessoa (idPessoa{coluna_dados})\
                VALUES ({idPessoa}, {dados})")
                mycursor.execute(f"INSERT INTO `pessoa jurídica` (CNPJ{coluna_dados})\
                VALUES ({CNPJ}, {dados})")
                
                # Ao inserir um novo cadastro, o usuário já vem "Ativado" por padrão.
                # id = mycursor.fetchall()
                meuDB.commit()
                resultado = True
            except mysql.connector.Error as error:
                print("Falha na inserção dos dados!: {}".format(error))
                meuDB.rollback()
                resultado = False
    
    def dados_conta():
        pass
    
    
#Inserir.endereço("01912841223", "76813848", "R. Escorpião", "11700", "s/c", "Ulisses Guimarães", "Porto Velho", "Rondônia")

#Inserir.dados_cliente_pf(CPF="01912841223", nome="Alefsander Ribeiro Nascimento", rg="1189307", orgão_RG="SESDEC/RO",
#                         data_emissão_RG="10/04/2010", data_nascimento="23/10/1994", sexo="Masculino", nacionalidade="Brasileiro",
#                         naturalidade="Porto Velho", nome_pai="João Nascimento de Souza", nome_mae="Edsandra Ribeiro de Souza")



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




