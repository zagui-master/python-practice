import os


def initialMessage():
    print("--------------------------------")
    print("  Welcome this is the new Crud ")
    print("")
    print("    There are our options    ")
    print("................................")
    print(" -1 = Create a new item")
    print(" -2 = Update an existing item")
    print(" -3 = Show all existing items")
    print(" -4 = Remove all existing items")
    print(" -5 = Finish the process")
    print("................................")


def invalidOptionMessage(option):
    os.system("cls")
    print("************************************")
    print("the option ", option, " is invalid ")
    print("************************************")


def finalMessage():
    os.system("cls")
    print("************************************")
    print("   Thank you for used our services")
    print("************************************")


