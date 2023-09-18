def solicitar_cadastro():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    return nome, email, senha

nome_usuario, email_usuario, senha_usuario = solicitar_cadastro()
print("Nome:", nome_usuario)
print("Email:", email_usuario)
print("Senha:", senha_usuario)