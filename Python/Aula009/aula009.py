x = "incrível"

def myFunc():
    global x
    x = "inacreditavel"
    y = "fantastico"
    global z 
    z = "Bem vindo"
    print("Python é "+ x  + "e" + y)
    print(z)


myFunc()

print("====================")
print("você é " + x)
print(z)


