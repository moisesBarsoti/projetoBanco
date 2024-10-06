import re
from datetime import datetime

emailRegex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
dataRegex = r'^\d{4}-\d{2}-\d{2}$'

class Cliente:
    def __init__(self, nomeDoCliente, sobrenomeDoCliente, dataDeAniversario, email, senha): 
        self.nomeDoCliente = nomeDoCliente
        self.sobrenomeDoCliente = sobrenomeDoCliente
        self.dataDeAniversario = datetime.strptime(dataDeAniversario, '%Y-%m-%d')
        self.email = email
        self.senha = senha
        self.saldo = 0  

    def getNome(self):
        return self.nomeDoCliente

    def getSobrenome(self):
        return self.sobrenomeDoCliente

    def getDataDeAniversario(self):
        return self.dataDeAniversario

    def getEmail(self):
        return self.email

    def getSenha(self):
        return self.senha

    def getSaldo(self):
        return self.saldo

    def calcularIdade(self):
        hoje = datetime.now()
        idade = hoje.year - self.dataDeAniversario.year - ((hoje.month, hoje.day) < (self.dataDeAniversario.month, self.dataDeAniversario.day))
        return idade
    
    def __str__(self) -> str:
        return f'{self.nomeDoCliente} {self.sobrenomeDoCliente} {self.dataDeAniversario} {self.email} {self.senha}'
    

# Recebendo valores
nome = input('Digite o seu \033[33mnome:\033[m ')
while nome == '':
    print(f'\033[31mVocê não pode deixar vazio!\033[m')
    nome = input('Digite o seu \033[33mnome:\033[m ')

sobrenome = input('Digite o seu \033[33msobrenome:\033[m ')
while sobrenome == '':
    print(f'\033[31mVocê não pode deixar vazio!\033[m')
    sobrenome = input('Digite o seu \033[33msobrenome:\033[m ')

data = input('Digite sua \033[33mdata de aniversário\033[m dessa forma \033[33m(ano-mês-dia):\033[m ')
while data == '':
    print(f'\033[31mVocê não pode deixar vazio!\033[m')
    data = input('Digite sua \033[33mdata de aniversário\033[m dessa forma \033[33m(ano-mês-dia):\033[m ')
while not re.match(dataRegex, data):
    print(f'\033[31mVocê tem que colocar dessa forma:\033[m')
    print(f'\033[36m2000-01-01\033[m')
    data = input('Digite sua \033[33mdata de aniversário\033[m dessa forma \033[33m(ano-mês-dia):\033[m ')

email = input('Digite o seu \033[33memail:\033[m ')
while email == '':
    print(f'\033[31mVocê não pode deixar vazio!\033[m')
    email = input('Digite o seu \033[33memail:\033[m ')
while not re.match(emailRegex, email):
    print(f'\033[31mVocê tem que colocar dessa forma:\033[m')
    print(f'\033[36mseuEmail@gmail.com\033[m')
    email = input('Digite o seu \033[33memail:\033[m ')

senha = input('Digite a sua \033[33msenha (digite até 6 números):\033[m ')
while not senha.isdigit() or len(senha) > 6:
    print(f'\033[31mVocê não pode deixar vazio e a senha deve ter até 6 números!\033[m')
    senha = input('Digite a sua \033[33msenha (digite até 6 números):\033[m ')

senhaINT = int(senha)

# Usando valores
pessoa = Cliente(nome, sobrenome, data, email, senhaINT)