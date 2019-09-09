import pyperclip
from os import system, name as os_name
import os


def clearScreen():
    # for windows
    if os_name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def AddAccount(name, password):
    if AccountExists(name):
        return False
    try:
        f = open("accounts.dat", "a")
        f.write(str(name) + ':' + str(password) + ':' + '\n')
        f.close()
        return True
    except:
        return False


def DeleteAccount(name):
    try:
        #Get all accounts into list
        accounts = []
        f = open("accounts.dat", "r")
        for _s in f:
            accounts.append(_s)
        #Clear file
        f = open('accounts.dat', 'r+')
        f.truncate(0)

        #Insert accounts again
        i = 0
        while i < len(accounts):
            if accounts[i].split(':')[0] == name:
                i += 1
                continue
            AddAccount(accounts[i].split(':')[0], accounts[i].split(':')[1])
            i += 1
        return True
    except:
        return False


def AccountExists(name):
    try:
        for _s in open("accounts.dat", "r"):
            if _s.split(':')[0] == name:
                return True
        return False
    except:
        return False


def GetPassword(name):
    for _s in open("accounts.dat", "r"):
        if _s.split(':')[0] == name:
            return _s.split(':')[1]
    return False


def ToClipboard(string):
    if not string:
        return False
    pyperclip.copy(string)
    return True


if __name__ == "__main__":
    while True:
        print("1. Get password to account\n2. Add new account\n3. Delete account\n4. Change password\n\nYour choice : ")
        choice = input()
        if choice == '1':
            clearScreen()
            print("Enter account : ")
            account = input()
            if ToClipboard(GetPassword(account)):
                print("Password is copied to clipboard")
            else:
                print("Account doesn't exist")

        if choice == '2':
            clearScreen()
            print("Enter account name : ")
            account = input()
            print("\nEnter password : ")
            password = input()
            if AddAccount(account, password):
                print("\nAccount successfully added!")
            else:
                print("\nError")

        if choice == '3':
            clearScreen()
            print("Enter account name : ")
            account = input()
            if DeleteAccount(account):
                print("Account successfully deleted")
            else:
                print("Error")

        if choice == '4':
            clearScreen()
            print("Enter account name : ")
            account = input()
            print("Enter new password : ")
            password = input()
            if not DeleteAccount(account):
                print("Error")
                break
            if not AddAccount(account, password):
                print("Error")
                break
            print("Password was changed successfully")
