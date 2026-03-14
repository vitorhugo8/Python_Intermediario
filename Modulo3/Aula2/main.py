import sqlite3
from pathlib import Path 

ROOT_DIR = Path(__file__).parent 
DB_NAME = "db_a2.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT,"
    "weight REAL"
    ")"
)

connection.commit() # Sem esse comando, as mudanças podem não ser gravadas no arquivo

# Registrar valores nas colunas da tabela 
def inserir_novos_valores(nome, peso):
    cursor.execute(
        f"INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)",
        (nome, peso)

    )
    connection.commit()

    print(f"Usuário '{nome}' adicionado com sucesso!")

# Mostrar usuários cadastrados 
def listar_usuarios():
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")

    usuarios = cursor.fetchall()

    print("\nUsuarios cadastrados no banco:")

    for usuario in usuarios:
        print(usuario)

# fluxo do programa 
inserir_novos_valores("Ana", 65.2)
inserir_novos_valores("João", 82.5)

listar_usuarios()

connection.close()