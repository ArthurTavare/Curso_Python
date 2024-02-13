x = "ola mundo"

try:
    print(x)
except NameError:
    print("este valor x nao foi encontrado")
except:
    print("Algo aconteceu")
else:
    print("sem nemhum erro no momento")
finally:
    print("o try excpt foi finalizado")

print("prosseguindo o programa")