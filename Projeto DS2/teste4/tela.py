

from conexao1 import conectar_bd
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")
janela.resizable(width=0, height=0)


def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()

    # Estabeleça a conexão com o banco de dados MySQL usando a função conectar_bd
    conn, cursor = conectar_bd()

    # Execute a instrução SQL para inserir os dados na tabela desejada (substitua 'sua_tabela' pelo nome correto da tabela)
    insert_query = "INSERT INTO clientes (nome, email, senha) VALUES (%s, %s, %s)"
    data = (nome, email, senha)

    try:
        cursor.execute(insert_query, data)
        conn.commit()
        print("Dados cadastrados com sucesso!")
    except Exception as e:
        conn.rollback()
        print(f"Erro ao cadastrar os dados: {e}")
    finally:
        conn.close()

    print(f"Cadastrando nome: {nome}, email: {email}, senha: {senha}")

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

botao = customtkinter.CTkButton(janela, text="Cadastrar", command=cadastrar)
botao.pack(padx=10, pady=10)

janela.mainloop()
