from classes.Cliente import pessoa
from barsotiBank import barsotiBank
from funcoes.barsotiBank import verSaldo
from funcoes.limpaTerminal import limparTerminal

import mysql.connector

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='205030',
    database='banco',
    auth_plugin='mysql_native_password'
)

cursor = conexao.cursor()

# Criação da tabela cliente com a coluna id
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cliente (
        nomeDoCLiente VARCHAR(255),
        sobrenomeDoCLiente VARCHAR(255),
        dataDeAniversario DATE,
        idade INT,
        email VARCHAR(255),
        senha VARCHAR(255)
    )
''')

# Inserção de dados na tabela cliente
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

# Criação da tabela barsotiBank
cursor.execute('''
    CREATE TABLE IF NOT EXISTS barsotiBank (
        nomeDoCliente VARCHAR(255),
        saldo DECIMAL(10, 2)
    )
''')

# Inserção de dados na tabela barsotiBank
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

# Selecionando as tabelas 
def selecionarTabelas():
    selectCliente = "SELECT * FROM cliente;"
    cursor.execute(selectCliente)
    resultadoCliente = cursor.fetchall()
    print(f"Tabela cliente: {resultadoCliente}")

    selectBarsotiBank = "SELECT * FROM barsotibank;"
    cursor.execute(selectBarsotiBank)
    resultadoBarsotiBank = cursor.fetchall()
    print(f"Tabela barsotiBank: {resultadoBarsotiBank}")

selecionarTabelas()    
print('')

# Apagar os valores 
def apagarValores():
    apagarValores = input(f"\033[33mDeseja apagar os valores das tabelas 'cliente' e 'barsotiBank'? (s ou n): \033[m").lower()

    if apagarValores == 's':
        limparTerminal()
        cursor.execute("DELETE FROM cliente;")
        cursor.execute("DELETE FROM barsotiBank;")
        conexao.commit()
        print(f"\033[32mValores das tabelas apagados com sucesso.\033[m")
        selecionarTabelas()
    else:
        limparTerminal()
        print(f"\033[32mValores das tabelas mantidos.\033[m")
        selecionarTabelas()

# Alterar valores
alterarValores = input(f"\033[33mDeseja fazer alguma alteração nos valores da tabela cliente? (s ou n): \033[m").lower()

if alterarValores == 's':
    limparTerminal()
    selecionarTabelas()
    
    nomeDoCliente = input(f"Digite o \033[33mnome\033[m do cliente que deseja alterar: ").capitalize()
    coluna = """
    Selecione a coluna, para alterar:
        
    [n] nomeDoCLiente 
    [s] sobrenomeDoCLiente
    [d] dataDeAniversario
    [i] idade
    [e] email
    [se] senha
    => """
    while True:
        opcao = input(coluna).lower()

        if opcao == 'n':
            coluna = 'nomeDoCLiente'
        elif opcao == 's':
            coluna = 'sobrenomeDoCLiente'
        elif opcao == 'd':
            coluna = 'dataDeAniversario'
        elif opcao == 'i':
            coluna = 'idade'
        elif opcao == 'e':
            coluna = 'email'
        elif opcao == 'se':
            coluna = 'senha'
        else:
            print(f"\033[31mSelecione uma opção váilida\033[m") 
                
        novoValor = input(f"Digite o novo valor para {coluna}: ")
        cursor.execute(f"UPDATE cliente SET {coluna} = %s WHERE nomeDoCLiente = %s", (novoValor, nomeDoCliente))
        limparTerminal()
        selecionarTabelas()

        conexao.commit()
        print(f"\033[32mValores atualizados com sucesso.\033[m")
        apagarValores()
        break
else:
    limparTerminal()
    apagarValores()


# Fechamento da conexão
cursor.close()
conexao.close()