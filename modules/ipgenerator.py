import random, os, time
from termcolor import colored

os.system('clear')

partialPath = input(colored("Write the path where you want to generate the file: ", 'white', 'on_blue'))
path = os.path.join(partialPath, 'ip_list.txt')

file = open(path, 'w')

message = colored("IP list generated on: {}".format(path), 'white', 'on_red')

def Generator():
    for i in range (0,244):
        rand1 = random.randint(0,254)
    return rand1

def ipAppend(string_, Quantity):
    auxList_ = string_.split('.')
    list_ = []
    for i in auxList_:
        list_.append(i.upper())
    if list_[-1] == 'XX' and list_[-2] != 'XX':
        for j in range(int(Quantity)):
            rand1 = Generator()
            print("{}.{}.{}.{}\n".format(list_[0],list_[1],list_[2],rand1))
            file.write("{}.{}.{}.{}\n".format(list_[0],list_[1],list_[2],rand1)) 
        file.close()
    elif (list_[-1] == 'XX') and (list_[-2] == 'XX') and list_[-3] != 'XX':
        for j in range(int(Quantity)):
            rand1 = Generator()
            rand2 = Generator()
            print("{}.{}.{}.{}\n".format(list_[0],list_[1],rand2,rand1))
            file.write("{}.{}.{}.{}\n".format(list_[0],list_[1],rand2,rand1))
        file.close()
    elif ((list_[-1] == 'XX') and (list_[-2] == 'XX')) and (list_[-3] == 'XX') and list_[-4] != 'XX':
        for j in range(int(Quantity)):
            rand1 = Generator()
            rand2 = Generator()
            rand3 = Generator()
            print("{}.{}.{}.{}\n".format(list_[0],rand3,rand2,rand1))
            file.write("{}.{}.{}.{}\n".format(list_[0],rand3,rand2,rand1))   
        file.close()
    elif ((list_[-1] == 'XX') and (list_[-2] == 'XX')) and ((list_[-3] == 'XX') and (list_[-4] == 'XX')):
        for j in range(int(Quantity)):
            rand1 = Generator()
            rand2 = Generator()
            rand3 = Generator()
            rand4 = Generator()
            print("{}.{}.{}.{}\n".format(rand4,rand3,rand2,rand1))
            file.write("{}.{}.{}.{}\n".format(rand4,rand3,rand2,rand1))      
        file.close()
    else:
        print(colored("ERROR", 'white','on_red'))

if __name__ == "__main__":
    os.system('clear')
    print(colord("Please, insert the range you want to generate with the following format:", 'white', 'on_green'))
    print(colored("192.168.xx.xx\n\n",'white','on_red'))
    opt = input(colored(">> ", 'white', 'on_red'))
    optQuantity = input(colored("Write the quantity of IP you want to generate: ", 'white', 'on_red'))
    ipAppend(opt, optQuantity)
    print(message)
    time.sleep(3)
