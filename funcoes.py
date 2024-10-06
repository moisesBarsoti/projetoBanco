from Cliente import pessoa

# Limpar terminal
import os
import platform

def limparTerminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


# Barsoti Bank
saldo = pessoa.getSaldo()
extrato = ""
numeroSaques = 0
limite = 500
LIMITE_SAQUES = 3

def opcaoBanco():
    menu = """
    Escolha uma das opções abaixo:
    
    [d] Depositar
    [s] Sacar
    [v] Ver Saldo
    [e] Extrato
    [x] Excluir Conta
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
        elif opcao == "v":
            print(f"Seu saldo é: R$ {verSaldo():.2f}")
        elif opcao == "x":
            excluirConta()
            break
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def depositar():
    global saldo, extrato
    valor = float(input("Informe o valor do depósito: "))
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print('Operação funcionou! Veja o extrato')
    else:
        print("Operação falhou! O valor informado é inválido.")

def saque():
    global saldo, extrato, numeroSaques
    valor = float(input("Informe o valor do saque: "))
    
    excedeuSaldo = valor > saldo
    excedeuLimite = valor > limite
    excedeuSaques = numeroSaques >= LIMITE_SAQUES
    
    if excedeuSaldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeuLimite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeuSaques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numeroSaques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
        
def verSaldo():
    print('')
    return saldo

def mostrarExtrato():
    global extrato, saldo
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def excluirConta():
    global saldo, extrato, numeroSaques
    saldo = 0
    extrato = ""
    numeroSaques = 0
    print("Conta excluída com sucesso.")