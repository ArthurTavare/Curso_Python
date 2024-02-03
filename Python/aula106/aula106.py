import re 

txt = "O calor do motor da moto"

x = re.search("\s", txt)

print("O primeiro espaco em branco esta na posicao:", x.start)

x = re.search("portugal", txt)
print(x)