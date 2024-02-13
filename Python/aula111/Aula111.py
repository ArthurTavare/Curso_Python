import re

# [] Um conjunto de caracteres "[a-m]"
txt = "O calor do motor da moto"
#Encontre todos os caracteres minúsculos em ordem alfabética entre "a" e "m":
x = re.findall("[a-m]", txt)
print(x)

# \ Sinaliza uma sequência especial (também pode ser usado para caracteres de escape) "\d"
txt = "Eu tenho 36 anos de idade"
x = re.findall("\d", txt)
print(x)

# .	Qualquer caractere (exceto caractere de nova linha)	"mu..o"
txt = "Ola mundo"
#Procure uma sequência que comece com "mu", seguido por dois (quaisquer) caracteres e um "o":
x = re.findall("mu..o", txt)
print(x)
