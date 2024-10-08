from classes.Cliente import pessoa

# Variáveis globais
saldo = pessoa.getSaldo()
extrato = ""
numeroSaques = 0
limite = 500
LIMITE_SAQUES = 3

# Menu de escolha
def opcaoBanco():
    menu = """
    Escolha uma das opções abaixo:
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [x] Excluir extrato
    [q] Sair
    => """
    
    while True:
        opcao = input(menu).lower()
        
        if opcao == "d":
            depositar()
        elif opcao == "s":
            saque()
        elif opcao == "e":
            mostrarExtrato()
        elif opcao == "x":
            excluirExtrato()
        elif opcao == "q":
            break
        else:
            print(f"\033[31mOperação inválida, por favor selecione novamente a operação desejada.\033[m")

# Depositar

def depositar():
    global saldo, extrato
    valor = float(input("Informe o valor do depósito: "))
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\033[32mOperação funcionou! Veja o extrato\033[m")
        print(f"\033[33mSeu saldo é:\033[m \033[32mR$ {verSaldo():.2f}\033[m")
    else:
        print(f"\033[31mOperação falhou! O valor informado é inválido.\033[m")

# Saque

def saque():
    global saldo, extrato, numeroSaques
    valor = float(input("Informe o valor do saque: "))
    
    excedeuSaldo = valor > saldo
    excedeuLimite = valor > limite
    excedeuSaques = numeroSaques >= LIMITE_SAQUES
    
    if excedeuSaldo:
        print(f"\033[31mOperação falhou! Você não tem saldo suficiente.\033[m")
    elif excedeuLimite:
        print(f"\033[31mOperação falhou! O valor do saque excede o limite.\033[m")
    elif excedeuSaques:
        print(f"\033[31mOperação falhou! Número máximo de saques excedido.\033[m")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numeroSaques += 1
        print(f"\033[32mOperação funcionou! Veja o extrato\033[m")
        print(f"\033[33mSeu saldo é:\033[m \033[32mR$ {verSaldo():.2f}\033[m")
    else:
        print(f"\033[31mOperação falhou! O valor informado é inválido.\033[m")


# Ver saldo
        
def verSaldo():
    print('')
    return saldo

# Mostrar extrato

def mostrarExtrato():
    global extrato, saldo
    print("\n================ EXTRATO ================")
    print(f"\033[33mNão foram realizadas movimentações.\033[m" if not extrato else extrato)
    print(f"\nSaldo: \033[32mR$ {saldo:.2f}\033[m")
    print("==========================================")

# Excluir extrato

def excluirExtrato():
    global saldo, extrato, numeroSaques
    saldo = 0
    extrato = ""
    numeroSaques = 0
    print(f"\033[32mExtrato excluído com sucesso.\033[m")