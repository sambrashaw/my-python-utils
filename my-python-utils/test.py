import hashlib
import getpass
import os, sys


def writedatabase(file, account):
    with open(file, "a") as f:
        f.write(",".join(account) + "\n")


def readdatabase(file):
    recordlist = []
    with open(file, "r") as f:
        for record in f.readlines():
            recordlist.append(record.replace("\n", "").split(","))
    return recordlist


def addaccount(username, passwd):
    writedatabase("database.txt", [username, passwd])


def clear():
    os.system("cls")


def changepassword(username):
    clear()
    print("┏" + "━" * 20 + "┓")
    print("┃" + " " * 2 + "Password Change" + " " * 2 + "┃")
    print("┗" + "━" * 20 + "┛\n")
    newpasswd = hashlib.sha256(getpass.getpass("Password: ").encode('utf-8')).hexdigest()
    database = readdatabase("database.txt")
    for account in database:
        if account[0] == username:
            account[1] = newpasswd
    makelogin(True)

def addaccountprompt():
    print("┏" + "━" * 20 + "┓")
    print("┃" + " " * 5 + "Add Account" + " " * 4 + "┃")
    print("┗" + "━" * 20 + "┛\n")
    username = input("Username: ")
    password = hashlib.sha256(getpass.getpass("Password: ").encode('utf-8')).hexdigest()
    addaccount(username, password)
    makelogin(True)


def accountoptions(username, flag):
    clear()
    print("┏" + "━" * 20 + "┓")
    print("┃" + " " * 2 + "Account Options" + " " * 3 + "┃")
    print("┗" + "━" * 20 + "┛\n")
    print("1) Change Password")
    if flag == "<*>":
        print("2) Add New Account (Administrator Only)")
        print("3) Sign out")
    else:
        print("2) Sign out")
    print("Q) Quit\n")
    option = input("Option: ")
    if option == "1":
        changepassword(username)
    elif option == "2":
        addaccountprompt()
    elif option == "3":
        makelogin(True)
    elif option.upper() == "Q":
        sys.exit()
    else:
        print("Input not correct. Use one of the given options.")
        accountoptions(username, flag)


def makelogin(status):
    clear()
    correct = False
    print("┏" + "━" * 20 + "┓")
    print("┃" + " " * 5 + "Login Form" + " " * 5 + "┃")
    print("┗" + "━" * 20 + "┛")
    if not status:
        print("Username or Password entered was not correct.")
    username = input("Username: ")
    password = hashlib.sha256(getpass.getpass("Password: ").encode('utf-8')).hexdigest()
    for account in readdatabase("database.txt"):
        if account[0] == username and account[1] == password:
            clear()
            print("You've been logged in.\n")
            try:
                accountflag = account[2]
            except IndexError:
                accountflag = ""
            correct = True
            accountoptions(account[0], accountflag)
    if not correct:
        makelogin(False)


makelogin(True)
