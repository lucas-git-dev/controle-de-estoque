import sqlite3

def connect():
    return sqlite3.connect('estoque.db')

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL     
                   )
    ''')
    conn.commit()
    conn.close()

# database.py (continuação)

def insert(nome, quantidade, preco):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
                   (nome, quantidade, preco))
    conn.commit()
    conn.close()

def read():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def update(id_produto, nome, quantidade, preco):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE produtos SET nome = ?, quantidade = ?, preco = ? WHERE id = ?",
                   (nome, quantidade, preco, id_produto))
    conn.commit()
    conn.close()

def delete(id_produto):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
    conn.commit()
    conn.close()
