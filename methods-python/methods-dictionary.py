"""
get =  look for an item by its key *
keys = generate a list in key from the register of dictionary *
values = generate a list in value  from the register of dictionary *
items = generate a lis in key-value from the register of dictionary *
pop = extract a register from a dictionary from its key and delete,
accept value by defect *
clear = delete all register from a dictionary

https://docs.hektorprofe.net/python/metodos-de-las-colecciones/metodos-de-los-diccionarios/
"""

data = {
    "name": "Sergio",
    "lastName": "Lopez",
    "age": 25,
    "address": "cra-4 #-2",
    "neighborhood": "Las americas",
    "email": "sal@gmail.com"
}

print("methods get()")
print("what contains the key name? : ", data.get("name"))
print("********************************************")
print("methods key()")
print(data.keys())
print("********************************************")
print("methods values()")
print(data.values())
print("********************************************")
print("methods items()")
print(data.items())
print("********************************************")
print("methods pop()")
print(data)
data.pop("email")
print(data)
print("********************************************")
print("methods clear()")
print(data)
data.clear()
print(data)
print("********************************************")
