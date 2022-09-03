
def media():
    count = 0
    numeros=[]

    while count != 3:

        count +=1
        print("Ingrese el valor numero ", count)
        numero= float(input("... "))
        numeros.append(numero)

    media = round(sum(numeros)/len(numeros))
    print("La media es : ", media)
