from classes.Cliente import pessoa
from funcoes.barsotiBank import opcaoBanco
from funcoes.limpaTerminal import limparTerminal

def barsotiBank():
    
    limparTerminal()
    
    # Verificação se é maior de idade
    if pessoa.calcularIdade() > 17:
        print(f'{pessoa.getNome().capitalize()}, Seja bem vindo a Barsoti Bank!')
    else:
        print(f'{pessoa.getNome().capitalize()} você é menor de idade')
        print('Saindo...')
        print('Saiu')


    # Informações do cliente
    print('')
    print(f'\033[36mSeu nome é:\033[m {pessoa.getNome().capitalize()}')
    print(f'\033[36mSeu sobrenome é:\033[m {pessoa.getSobrenome().capitalize()}')
    print(f'\033[36mSua idade é:\033[m {pessoa.calcularIdade()}')
    print(f'\033[36mSeu email é:\033[m {pessoa.getEmail()}')
    print(f'\033[36mSua senha é:\033[m {pessoa.getSenha()}')
    print('')
    print(f'\033[33mSeu saldo é:\033[m \033[32mR$ {pessoa.getSaldo()}\033[m')
    print('')

    # Opções de banco 
    opcaoBanco()