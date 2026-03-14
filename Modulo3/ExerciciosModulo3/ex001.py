import sqlite3
from pathlib import Path 

# Caminho do banco 
ROOT_DIR = Path(__file__).parent
DB_FILE = ROOT_DIR / "db.sqlite3"

# Criando a Tabela no Banco de Dados 
def create_table():
    with sqlite3.connect(DB_FILE) as conn: # Utilizando o 'with', abrimos a coenxão e, depois de usar, ela fecha automáticamente
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """)
        
def add_user(nome, email):       
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO usuarios (nome, email) VALUES (?, ?)", 
            (nome, email)
            # Proteção contra SQL Injection chamada Prepared Statment  
        )

def list_users():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios")

        usuarios = cursor.fetchall()

        for usuario in usuarios:
            print(usuario)

# fluxo do programa 
create_table()

add_user("Ana", "ana@email.com")
add_user("Carlos", "carlos@email.com")

print("Usuários cadastrados com sucesso:")
list_users()