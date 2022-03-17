import random 
import os, sys, time
from termcolor import colored
from modules import macchanger

def menu():
    os.system('clear')
    print(colored(">>> ", 'white', 'on_blue') + colored("IP UTILITY ", 'white', 'on_green') + colored("<<<", 'white', 'on_blue') + "\n\n")
    print(colored("[1] ",'white','on_green') + colored("Mac Changer",'white','on_blue'))
    print(colored("[2] ",'white','on_green') + colored("Random IP Generator",'white','on_blue'))
    print(colored("[3] ", 'white', 'on_green') + colored("IP Analyzer",'white','on_blue') + "\n")
    print(colored("[4] ", 'white', 'on_green') + colored("Exit", 'white', 'on_red') + "\n\n")
    option = int(input(colored("Choose your option: ", 'white', 'on_green')))
    
    return option

if __name__ == "__main__":
    while True:
        option = menu()
    
        if option == 1:
            macchanger.menu()
        elif option == 2:
            from modules import ipgenerator
        elif option == 3:
            pass
        elif option == 4:
            sys.exit()
        else:
            print(colored("\nIncorrect Option", 'white', 'on_red'))
            time.sleep(3)
