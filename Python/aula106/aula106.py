import re

txt = "O calor do motor da moto"

x = re.search("\s", txt)

print("O primeiro espaço em branco esta na posição:", x.start())

x = re.search("Portugal", txt)
print(x)
