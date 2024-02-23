f = open("demofile.txt", "x")

f = open("demofile.txt", "w",encoding="UTF-8")
f.write("Opa! Sobrescrevi o conteudo./n")
f.close()

f = open("demofile.txt", "w",encoding="UTF-8")
print(f.read())
f.close