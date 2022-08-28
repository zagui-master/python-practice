import os



def createANewItem(items):
    os.system("cls")
    print("-----------------------------------------")
    print('.... You are select Create a new item....')
    item = input('.... Enter the new item... ')
    items.append(item)
    os.system("cls")
    print(item, ' was created successfully ')
    return items


def showItems(items):
    os.system("cls")
    if len(items) != 0:
        print("-----------------------------------------")
        print('... Your are select Show all items ')
        print('... Item(s)')
        for item in items:
            print('  *', item)
    else:
        print("-----------------------------------------")
        print('... Your are select Show all items ')
        print("... The list don't have items")
        print("... First you need create an item and comeback")


def removeAllItems(items):
    os.system("cls")
    items.clear()
    print("-----------------------------------------")
    print('... Your are select Remove all items ')
    print("... The items was removed")
    return items


def updateItems(items):
    print("........There are our options........")
    print(" -1 = Add an element in at specific position")
    print(" -2 = Remove an element at a specific position")
    option2 = int(input('  Please enter an option ... '))

    while option2 < 1 or option2 > 2:
        """
        messages.invalidOptionMessage(option2)

        """
        print("there are the elements")
        for value in items:
            print("postion = ",items.index(value)," value : ", value)

        print("Select the element to remove")
        position = int(input("Enter the position..."))
        value = int(input("Enter the element to remove..."))
        items.remove(value)
        return items

"""
create a new item an specific position
and delete an specific option
"""