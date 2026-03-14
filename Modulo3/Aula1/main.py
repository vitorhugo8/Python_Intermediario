import sqlite3 
from pathlib import Path 
## A biblioteca pathlib serve para manipular caminhos de arquivos de forma mais moderna os.path

ROOT_DIR = Path(__file__).parent 
# Pegando a pasta onde o arquivo está localizado
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE) # Recebe o arquivo
cursor = connection.cursor() # Cria um objeto cursor, usado para executar comandos SQL

cursor.close() 
connection.close() # Fecha a conexão com o banco
# SEMPRE que abrimos alguma coisa no Python, devemos fechar no fim do programa