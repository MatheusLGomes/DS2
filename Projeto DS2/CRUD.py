import sqlite3



# Função para cadastrar um novo cliente
def cadastrar_cliente(email, senha):
    cursor.execute("INSERT INTO clientes (email, senha) VALUES (?, ?)", (email, senha))
    conn.commit()

# Função para listar todos os clientes
def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    return cursor.fetchall()

# Função para buscar um cliente por ID
def buscar_cliente(id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

# Função para atualizar os dados de um cliente
def atualizar_cliente(id, novo_email, nova_senha):
    cursor.execute("UPDATE clientes SET email=?, senha=? WHERE id=?", (novo_email, nova_senha, id))
    conn.commit()

# Função para deletar um cliente
def deletar_cliente(id):
    cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
    conn.commit()
