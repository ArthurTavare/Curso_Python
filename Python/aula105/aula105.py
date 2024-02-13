import re

txt = "O Gabriel amigo do Miguel"

#Verificar se a string começa com "O" e termina com "Miguel"

x = re.search("^O.*Miguel$", txt)

if x:
    print("SIM! Nos temos uma correspondência!")
else:
    print("Nenhuma correspondência!")
