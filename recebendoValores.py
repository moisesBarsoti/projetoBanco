class Cliente:
    def __init__ (
        self,
        nomeDoCLiente,
        sobrenomeDoCLiente,
        dataDeAniversario,
        email,
        senha
    ): 
        self.nomeDoCLiente = nomeDoCLiente,
        self.sobrenomeDoCLiente = sobrenomeDoCLiente,
        self.dataDeAniversario = dataDeAniversario,
        self.email = email,
        self.senha = senha
    
    def entrarNaConta(
            self,
            email,
            senha
            ):
            self.email = email
            self.senha = senha

    def saldo(self):
        return f'O seu saldo é: {self.saldo}'

    def sacar(self, valor):
        if (self.saldo > valor):
             print(f"Você não pode sacar R${valor}, o seu saldo é de {self.saldo}")
        else:     
            self.saldo -= valor

    def depositar(self, valor):
        if (valor <= 0):
             print("Você não pode depositar R$0")
        else:
             self.saldo += valor     

    def sair(self):
        print("Saindo.......")
        print("Saiu")

    def excluirConta(self):
        return f'Conta Excluida'
    
    def __str__(self) -> str:
         return f'{self.nomeDoCLiente}{self.sobrenomeDoCLiente}{self.dataDeAniversario}{self.email}{self.senha}'


nome = input(f'Digite o seu \033[33mnome:\033[m ')
sobrenome = input(f'Digite o seu \033[33msobrenome:\033[m ')
data = input(f'Digite sua \033[33mdata de aniversário\033[m dessa forma \033[33m(ano-mês-dia):\033[m ')
email = input(f'Digite o seu \033[33memail:\033[m ')
senha = int(input(f'Digite a sua \033[33msenha (digite até 6 números):\033[m '))

pessoa = Cliente(nome, sobrenome, data, email, senha)
print(pessoa)