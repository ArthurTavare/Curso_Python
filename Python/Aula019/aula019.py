print (10 > 9)  
print(10 == 9)
print(10 < 9)

a = 200
b = 330

if b > a:
    print("Sim , b é maior do que a ")
else:
    print("Não , b nao maior do que a ")

print (bool("olá"))
print (bool(15))
(bool(["apple", "cherry" , "Banana"]))
x = 0
y = ""
print(bool(x))
print(bool(y))

# Valores que retornam falso
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

def myFunction():
    return True

print(myFunction())

if myFunction():  
    print("sim!")
else:
    print("nao!")

x = 200
print(isinstance(x, int))