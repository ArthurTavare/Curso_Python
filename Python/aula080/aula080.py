class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Arthur", 14)
print("P1" , p1.nome)
print("P1" , p1.idade)

p2 = Pessoa("Danny",35)
print("P2" , p2.nome)
print("P2" , p2.idade)
