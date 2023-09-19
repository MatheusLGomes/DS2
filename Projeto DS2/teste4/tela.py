# Importa a função conectar_bd do arquivo conexao1
from conexao1 import conectar_bd
# Importa a biblioteca customtkinter para criar a interface gráfica
import customtkinter

# Configura a aparência da interface gráfica com um tema escuro
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Cria uma janela com dimensões 500x300 que não pode ser redimensionada pelo usuário
janela = customtkinter.CTk()
janela.geometry("300x500")
janela.resizable(width=0, height=0)

# Variável global para armazenar o ID do registro que será atualizado
id_atualizar = None
id_excluir = None

# Função que é chamada quando o botão "Cadastrar" é clicado
def cadastrar():
    # Obtém os valores dos campos de entrada
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()

    # Estabelece uma conexão com um banco de dados MySQL usando a função conectar_bd
    conn, cursor = conectar_bd()

    # Define a instrução SQL para inserir os dados em uma tabela 
    insert_query = "INSERT INTO clientes (nome, email, senha) VALUES (%s, %s, %s)"
    data = (nome, email, senha)

    try:
        # Executa a instrução SQL para inserir os dados
        cursor.execute(insert_query, data)
        conn.commit()  # Confirma as alterações no banco de dados
        print("Dados cadastrados com sucesso!")
    except Exception as e:
        conn.rollback()  # Desfaz as alterações no caso de erro
        print(f"Erro ao cadastrar os dados: {e}")
    finally:
        conn.close()  # Fecha a conexão com o banco de dados

    print(f"Cadastrando nome: {nome}, email: {email}, senha: {senha}")

def listar_dados():

    conn, cursor = conectar_bd()
    select_query = "SELECT * FROM clientes"

    try:
        cursor.execute(select_query)
        dados = cursor.fetchall()

        for dado in dados:
            print("Nome:", dado[1])
            print("Email:", dado[2])
            print("Senha:", dado[3])
            print()
    except Exception as e:
        print(f"Erro ao recuperar os dados: {e}")
    finally:
        conn.close()        

# Função para atualizar um registro no banco de dados
def atualizar():
    global id_atualizar
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()

    if id_atualizar is not None:
        # Estabeleça a conexão com o banco de dados MySQL usando a função conectar_bd
        conn, cursor = conectar_bd()

        # Execute a instrução SQL para atualizar o registro na tabela desejada 
        update_query = "UPDATE clientes SET nome = %s, email = %s, senha = %s WHERE id = %s"  
        data = (nome, email, senha, id_atualizar)

        try:
            cursor.execute(update_query, data)
            conn.commit()
            print("Registro atualizado com sucesso!")
            id_atualizar = None  # Redefina o ID para evitar atualizações acidentais
        except Exception as e:
            conn.rollback()
            print(f"Erro ao atualizar o registro: {e}")
        finally:
            conn.close()
    else:
        print("Nenhum registro selecionado para atualização.")    

# Função para excluir um registro do banco de dados
def excluir():
    global id_excluir

    if id_excluir is not None:
        # Estabeleça a conexão com o banco de dados MySQL usando a função conectar_bd
        conn, cursor = conectar_bd()

        # Execute a instrução SQL para excluir o registro na tabela desejada 
        delete_query = "DELETE FROM clientes WHERE id = %s"  
        data = (id_excluir,)

        try:
            cursor.execute(delete_query, data)
            conn.commit()
            print("Registro excluído com sucesso!")
            id_excluir = None 
        except Exception as e:
            conn.rollback()
            print(f"Erro ao excluir o registro: {e}")
        finally:
            conn.close()
    else:
        print("Nenhum registro selecionado para exclusão.")



# Cria rótulos, campos de entrada, caixa de seleção e botão na interface gráfica
texto = customtkinter.CTkLabel(janela, text="Fazer Cadastro")
texto.pack(padx=10, pady=10)

entry_nome = customtkinter.CTkEntry(janela, placeholder_text="Seu nome")
entry_nome.pack(padx=10, pady=10)

entry_email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
entry_email.pack(padx=10, pady=10)

entry_senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
entry_senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)

botao_cadastro = customtkinter.CTkButton(janela, text="Cadastrar", command=cadastrar)
botao_cadastro.pack(padx=10, pady=10)

botao_listar = customtkinter.CTkButton(janela, text="Listar", command=listar_dados)
botao_listar.pack(padx=10, pady=10)

botao_atualizar = customtkinter.CTkButton(janela, text="Atualizar", command=atualizar)
botao_atualizar.pack(padx=10, pady=10)

botao_excluir = customtkinter.CTkButton(janela, text="Excluir", command=excluir)
botao_excluir.pack(padx=10, pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()
