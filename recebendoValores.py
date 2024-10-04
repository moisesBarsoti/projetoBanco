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
        self.senha = senha,

    def novaConta(
            self,
            nomeDoCLiente,
            sobrenomeDoCLiente,
            dataDeAniversario,
            email,
            senha
            ):
            self.nomeDoCLiente = nomeDoCLiente
            self.nomeDoCLiente = nomeDoCLiente
            self.sobrenomeDoCLiente = sobrenomeDoCLiente
            self.dataDeAniversario = dataDeAniversario
            self.email = email
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

pessoa = Cliente('Moises','Barsoti','2005-07-03','teste2@gmail.com',1234)
print(pessoa)