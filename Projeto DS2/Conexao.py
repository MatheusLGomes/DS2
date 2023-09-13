import mysql.connector

conn = mysql.connector.connect(host='localhost', database='datamatheus ',user='root', password='')

if conn.is_connected():
    db_info = conn.get_server_info()
    print("Conectado ao servidor MySQL", db_info)

    cursor = conn.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)