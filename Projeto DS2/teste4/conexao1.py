# Importa o módulo mysql.connector, que permite a conexão com o MySQL.
import mysql.connector 

# Função para estabelecer a conexão e retornar a conexão e o cursor.
def conectar_bd():
    conn = mysql.connector.connect(host='localhost', database='datamatheus', user='root', password='')
    cursor = conn.cursor()
    return conn, cursor

# Chama a função para conectar ao banco de dados.
conn, cursor = conectar_bd()

# Verifica se a conexão foi estabelecida com sucesso.
if conn.is_connected():
    # Obtém informações sobre a versão do servidor MySQL.
    db_info = conn.get_server_info()
    print("Conectado ao servidor MySQL", db_info)

# Executa uma consulta SQL para obter o nome do banco de dados atual.
cursor.execute("select database(); ")

# Recupera a primeira linha do resultado da consulta.
linha = cursor.fetchone()

# Exibe o nome do banco de dados ao qual você está conectado.
print("Conectado ao banco de dados ", linha)
