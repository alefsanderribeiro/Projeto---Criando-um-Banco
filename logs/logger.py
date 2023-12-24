import datetime #biblioteca para informar a data e para criar os arquivos de log.
import logging #bilioteca para geração de LOG.
from pathlib import Path #biblioteca para manipulação de diretórios.

local_log = Path() / "logs"

t = datetime.datetime.now() # informar a data e hora de agora.
agora_dia = t.strftime("%d-%m-%Y") # modificar a data para um formato de melhor entendimento.
agora_hora = t.strftime("%H-%M-%S") # modificar a hora para um formato de melhor entendimento.

Arquivo_log = local_log / f"{agora_dia}"

if Arquivo_log.exists() == False:
    Path.mkdir(Arquivo_log) #Caso não tenha a pasta com a data do dia, será criada uma nova

logging.basicConfig(level=logging.INFO, # o level de log que é para mostrar.
                    filename=Arquivo_log / f"{agora_hora}.txt", # "filename" já cria um arquivo, caso não exista.
                    format="%(asctime)s - %(levelname)s - %(message)s") # formato de mostrar no LOG.

