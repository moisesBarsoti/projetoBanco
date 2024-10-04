import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '205030',
    database = 'cadastrodeusuario2',
    auth_plugin = 'mysql_native_password'
) 

cursor = conexao.cursor()

comando = f'''

    DELETE from vendas WHERE nomeDoProduto = "Chocolate";

'''

cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()



# CREATE

# nomeDoProduto = "Chocolate"
# valor = 10

# comando = f'''
#     INSERT INTO vendas (
#         nomeDoProduto,
#         valor
#     ) VALUES (
#         "{nomeDoProduto}",
#         {valor}
#     );

# '''

# cursor.execute(comando)
# conexao.commit()

# cursor.close()
# conexao.close()


# READ

# cursor = conexao.cursor()

# comando = f'''

#     SELECT * FROM vendas;

# '''

# cursor.execute(comando)

# resultado = cursor.fetchall()
# print(resultado)

# conexao.commit()



# cursor.close()
# conexao.close()

# UPDATE

# cursor = conexao.cursor()

# comando = f'''

#     UPDATE vendas SET valor = 8 WHERE nomeDoProduto = "Chocolate";

# '''

# cursor.execute(comando)
# conexao.commit()

# cursor.close()
# conexao.close()

# DELETE

