"""
    -1 = Create a new item *
    -2 = Update an existing item **
    -3 = Show all existing items *
    -4 = Delete all existing items *
    -5 = Finish the process *
"""

import os
from modules import messages
from modules import actions

defaultProps = 'Welcome Stranger'
items = [1,2,3,4,5]

messages.initialMessage()

option = int(input('  Please enter an option ... '))
os.system("cls")

while option <= 0 or option > 5:
    messages.invalidOptionMessage(option)
    messages.initialMessage()
    option = int(input('  Please enter an option ... '))
    os.system("cls")

else:
    while option != 5:

        if option == 1:
            actions.createANewItem(items)
            messages.initialMessage()
            option = int(input('  Please enter an option ... '))

            while option <= 0 or option > 5:
                messages.invalidOptionMessage(option)
                messages.initialMessage()
                option = int(input('  Please enter an option ... '))
                os.system("cls")

        if option == 2:
            print("option 2 is an experimental function, please continue with another option")

            """
            actions.updateItems(items)
            """
            messages.initialMessage()
            option = int(input('  Please enter an option ... '))

            while option <= 0 or option > 5:
                messages.invalidOptionMessage(option)
                messages.initialMessage()
                option = int(input('  Please enter an option ... '))
                os.system("cls")

        if option == 3:
            actions.showItems(items)
            messages.initialMessage()
            option = int(input('  Please enter an option ... '))

            while option <= 0 or option > 5:
                messages.invalidOptionMessage(option)
                messages.initialMessage()
                option = int(input('  Please enter an option ... '))
                os.system("cls")

        if option == 4:
            actions.removeAllItems(items)
            messages.initialMessage()
            option = int(input('  Please enter an option ... '))

            while option <= 0 or option > 5:
                messages.invalidOptionMessage(option)
                messages.initialMessage()
                option = int(input('  Please enter an option ... '))
                os.system("cls")

messages.finalMessage()
