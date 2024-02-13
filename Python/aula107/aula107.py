import re

txt = "O calor do motor da moto"

x = re.findall("or", txt)
print(x)

# x = re.findall("Portugal", txt)

if x:
    print("Sim, existe pelo menos uma correspondência!")
else:
    print("Sem correspondências")
