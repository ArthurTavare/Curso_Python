x = "ola mundo!"

try:
    print(x)
except NameError:
    print("variavel nao definida")
except:
    print("Aconteceu uma excecao")

    print("continuando programa")
else:
    print("tudo certo por aqui")

print("Continuar programar")