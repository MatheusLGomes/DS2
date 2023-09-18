import customtkinter  # Importa a biblioteca customtkinter, que provavelmente é uma biblioteca personalizada de Tkinter

customtkinter.set_appearance_mode("dark")  # Define o modo de aparência como "dark" (escuro)
customtkinter.set_default_color_theme("dark-blue")  # Define o tema de cor padrão como "dark-blue" (azul escuro)

janela = customtkinter.CTk()  # Cria uma instância da janela principal usando a biblioteca customtkinter
janela.geometry("500x300")  # Define a geometria da janela como 500 pixels de largura por 300 pixels de altura
janela.resizable(width=0, height=0)  # Impede que a janela seja redimensionada pelo usuário

# Crie os campos de entrada como variáveis globais
entry_nome = None  # Declara uma variável global para o campo de entrada do nome (ainda não inicializada)
entry_email = None  # Declara uma variável global para o campo de entrada do email (ainda não inicializada)
entry_senha = None  # Declara uma variável global para o campo de entrada da senha (ainda não inicializada)

def cadastrar():  # Define uma função chamada "cadastrar"
    nome = entry_nome.get()  # Obtém o valor do campo de entrada do nome
    email = entry_email.get()  # Obtém o valor do campo de entrada do email
    senha = entry_senha.get()  # Obtém o valor do campo de entrada da senha
    # Aqui você pode fazer o que quiser com os dados, por exemplo, enviá-los para o backend
    print(f"Cadastrando nome: {nome}, email: {email}, senha: {senha}")

texto = customtkinter.CTkLabel(janela, text="Fazer Cadastro")  # Cria um rótulo na janela com o texto "Fazer Cadastro"
texto.pack(padx=10, pady=10)  # Empacota o rótulo na janela com margens de 10 pixels

entry_nome = customtkinter.CTkEntry(janela, placeholder_text="Seu nome")  # Cria um campo de entrada com um marcador de posição para o nome
entry_nome.pack(padx=10, pady=10)  # Empacota o campo de entrada na janela com margens de 10 pixels

entry_email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")  # Cria um campo de entrada com um marcador de posição para o email
entry_email.pack(padx=10, pady=10)  # Empacota o campo de entrada na janela com margens de 10 pixels

entry_senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")  # Cria um campo de entrada com um marcador de posição para a senha (os caracteres são exibidos como asteriscos)
entry_senha.pack(padx=10, pady=10)  # Empacota o campo de entrada na janela com margens de 10 pixels

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar Login")  # Cria uma caixa de seleção com o texto "Lembrar Login"
checkbox.pack(padx=10, pady=10)  # Empacota a caixa de seleção na janela com margens de 10 pixels

botao = customtkinter.CTkButton(janela, text="Cadastrar", command=cadastrar)  # Cria um botão com o texto "Cadastrar" que chamará a função "cadastrar" quando clicado
botao.pack(padx=10, pady=10)  # Empacota o botão na janela com margens de 10 pixels

janela.mainloop()  # Inicia o loop principal da janela Tkinter, que mantém a janela aberta e responde às interações do usuário
