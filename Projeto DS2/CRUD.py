from Conexao import conectar_bd

def inserir_dados(nome, email, senha):
    conn, cursor = conectar_bd()
    

     # Valores que você deseja inserir na tabela clientes.
    nome_cliente = "Matheus"
    email_cliente = "matheus@gmail.com"
    senha_cliente = "1234"




    # Comando SQL para inserção de dados.
    sql = "INSERT INTO clientes(nome, email,senha) VALUES (%s, %s, %s)"
    valores = (nome_cliente, email_cliente, senha_cliente)
    
    try:
        cursor.execute(sql, valores)
        conn.commit()  # Confirma a transação no banco de dados.
        print("Dados inseridos com sucesso!")
    except Exception as e:
        print("Erro ao inserir dados:", e)
    finally:
        cursor.close()
        conn.close()

