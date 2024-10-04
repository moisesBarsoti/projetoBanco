import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '205030',
    database = 'banco',
    auth_plugin = 'mysql_native_password'
)

cursor = conexao.cursor()

comando = f'''

    INSERT INTO cliente (
        nomeDoCLiente,
        sobrenomeDoCLiente,
        dataDeAniversario,
        email,
        senha
    ) VALUES (
        "Moisés",
        "Barsoti",
        "2005-07-03",
        "teste123@gmail.com",
        123456
    );

'''

cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()