from termcolor import colored
import subprocess
import random
import time
import sys, os
import psutil

characters = ['a', 'b', 'c', 'd', 'e', 'f',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
even = ['2', '4', '6', '8', '0']

#With this function you can generate a random mac address
def randomMacGenerator():
    empty_string = ""
    a = "{a}{a2}".format(a = random.choice(characters), a2 = random.choice(even))   #First octect must be an even number
    b = "{b}{b2}".format(b = random.choice(characters), b2 = random.choice(characters))
    c = "{c}{c2}".format(c = random.choice(characters), c2 = random.choice(characters))
    d = "{d}{d2}".format(d = random.choice(characters), d2 = random.choice(characters))
    e = "{e}{e2}".format(e = random.choice(characters), e2 = random.choice(characters))
    f = "{f}{f2}".format(f = random.choice(characters), f2 = random.choice(characters))
    
    mac = empty_string.join("{a_}:{b_}:{c_}:{d_}:{e_}:{f_}".format(a_ = a, b_ = b,
        c_ = c, d_ = d, e_ = e, f_ = f))
    

    return mac

def interfacesShow():
    try:
        interfaces = psutil.net_if_addrs()
        interfaces = '{}'.format(interfaces.keys()) 
        return interfaces
    except Exeption as e:
        pass

#Changer your mac address once
def macChanger():
    print(colored("Available networks:", 'white', 'on_blue'))
    print("\n" + interfacesShow() + "\n")
    inter = input(colored("Select your interface: ", 'white', 'on_blue'))
    new_mac = randomMacGenerator()

    try:
        os.system("clear")
        print(colored("[+]", 'white', 'on_green') + colored("Changing MAC Address to {}".format(new_mac), 'white', 'on_blue'))
        time.sleep(3)
        subprocess.call("ifconfig {} down ".format(inter), shell = True)
        subprocess.call("ifconfig {a} hw ether {b}".format(a = inter, b = new_mac), shell = True)
        subprocess.call("ifconfig {} up".format(inter), shell = True)
        print(colored("MAC Address change done", 'white', 'on_blue'))
    except Exception as e:
        print(colored("Error while running the code :(", 'white', 'on_red'))
        time.sleep(3)

#This function change your mac address in a certain time interval
def dinamicMacChanger():
    try:
        os.system("clear")
        time_ = input(colored("Set the change interval (sec):  ", 'white','on_green'))
        print(colored("Avaible networks: ", 'white', 'on_blue'))
        print("\n" + interfacesShow() + "\n")
        inter = input(colored("Select your interface: ", 'white', 'on_blue'))
        while True:
            new_mac = randomMacGenerator()
            subprocess.call("ifconfig {} down".format(inter), shell = True)
            subprocess.call("ifconfig {a} hw ether {b}".format(a = inter, b = new_mac), shell = True)
            subprocess.call("ifconfig {} up".format(inter), shell = True)
            print("Mac changed to: {}".format(new_mac))
            time.sleep(int(time_))
    except KeyboardInterrupt:
        print("\n[+] Leaving")
        time.sleep(3)
        pass
                

def menu():
    os.system("clear")
    print(colored(">>> MAC UTILS <<<", 'white', 'on_red'))
    print("")
    print(colored("[1] ", 'white', 'on_green') + colored("See available network interfaces", 'white', 'on_blue'))
    print(colored("[2] ", 'white', 'on_green') + colored("Change MAC", 'white', 'on_blue'))
    print(colored("[3] ", 'white', 'on_green') + colored("Dynamically MAC changer", 'white', 'on_blue'))
    print(colored("[4] ", 'white', 'on_green') + colored("EXIT", 'white', 'on_red'))
    
    opt = input(colored("Select your option: ", 'white', 'on_blue'))
    opt = str(opt)
    try:
        if opt == "1":
            print(interfacesShow())
            input("Press enter to return to menu")
            menu()
        elif opt == "2":
            macChanger()
            input("Press enter to return to menu")
            menu()
        elif opt == "3":
            dinamicMacChanger()
        elif opt == "4":
            sys.exit()
    except Exception as e:
        print(colored("Error runing the code", 'white', 'on_red'))
        time.sleep(3)
        menu()


