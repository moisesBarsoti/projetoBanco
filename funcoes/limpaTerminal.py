# Limpar terminal
import os
import platform

def limparTerminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')