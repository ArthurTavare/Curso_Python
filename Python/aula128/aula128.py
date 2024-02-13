x = 5

if x <0:
    raise Exception("nao sao permitidos numros negativos")

y = 10

if not type(y) is int:
    raise TypeError("somente numeros")

print("Fim do programa")