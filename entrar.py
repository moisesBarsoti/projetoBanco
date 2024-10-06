# Entrar / Cadastrar
import mysql.connector

def entrar():
    emailDeEntrar = input("Coloque seu email: ")
    senhaDeEntrar = input("Coloque sua senha: ")

    # Conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='205030',
        database='banco',
        auth_plugin='mysql_native_password'
    )

    cursor = conexao.cursor()

    # Consulta SQL para buscar o email e a senha do usuário
    consulta = "SELECT email, senha FROM cliente WHERE email = %s"
    cursor.execute(consulta, (emailDeEntrar,))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        emailBanco, senhaBanco = resultado
        if emailDeEntrar == emailBanco and senhaDeEntrar == senhaBanco:
            opcaoBanco()
        else:
            print("Senha incorreta!")
    else:
        print("Usuário não encontrado!")

def opcaoBanco():
    print("Bem-vindo ao banco!")

def cadastrar():
    print("Você se cadastrou no sistema.")

def entrarOuCadastrar():
    menuDeEntrar = """
    
    Seja bem vindo a Barsoti Bank
    
    [e] Entrar
    [c] Cadastre-se
    => """

    while True:
        opcao = input(menuDeEntrar).lower()
        
        if opcao == 'e':
            entrar()
            break
        elif opcao == 'c':
            cadastrar()
            break
        else:
            print("Opção inválida. Tente novamente.")
