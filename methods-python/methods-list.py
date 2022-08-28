"""
append = add a new item *
clear = delete all items
extend = join  a list to another list *
count = count how many times is an item in the list *
index = return the index at which an element appears *
insert = add a new item to a list in the specific index *
pop = extract an item from the list and delete this item *
remove = delete the first item from the list whose value coincides with what we indicate *
reverse = Flips the current list *
sort = order automatic the items from a list by its value of less a mayor
https://docs.hektorprofe.net/python/metodos-de-las-colecciones/metodos-de-las-listas/
"""

defaultData = "Master"
listOne = [defaultData]
listTwo = [defaultData + "name"]

listOne.append("sergio")
listOne.extend(listTwo)
print("How many time is sergio in ListOne : ", listOne.count("sergio"))
print("sergio is in the position : ", listOne.index("sergio"))
print(listOne)
listOne.insert(3, "uno mas ")
print(listOne)
listOne.pop(0)
print(listOne)
listOne.remove("sergio")
print(listOne)
listOne.reverse()
print(listOne)
listOne.sort()
print(listOne)



