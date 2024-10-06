from Cliente import pessoa
from barsotiBank import barsotiBank
from funcoes import verSaldo

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='205030',
    database='banco',
    auth_plugin='mysql_native_password'
)

cursor = conexao.cursor()

# Tabela cliente
clienteTabela = '''
    INSERT INTO cliente (
        nomeDoCLiente,
        sobrenomeDoCLiente,
        dataDeAniversario,
        idade,
        email,
        senha
    ) VALUES (%s, %s, %s, %s, %s, %s)
'''

cliente = (
    pessoa.getNome().capitalize(),
    pessoa.getSobrenome().capitalize(),
    pessoa.getDataDeAniversario(),
    pessoa.calcularIdade(),
    pessoa.getEmail(),
    pessoa.getSenha()
)

cursor.execute(clienteTabela, cliente)

# Usando barsotiBank
barsotiBank()

# Tabela Barsoti Bank
barsotiBankTabela = '''
    INSERT INTO barsotiBank (
        nomeDoCliente,
        saldo
    ) VALUES (%s, %s)
'''

barsotiBankValores = (
    pessoa.getNome().capitalize(),
    verSaldo()
)

cursor.execute(barsotiBankTabela, barsotiBankValores)
conexao.commit()

cursor.close()
conexao.close()