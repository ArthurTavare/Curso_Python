import os

os.system("cls") or None

while True:
    ValIni = input("digite o Valor inicial: ")
    ValIni = int(ValIni)
    if ValIni > 0:
        break

print()

while True:
    Valfin = input("digite o Valor Final: ")
    Valfin = int(Valfin)
    if ValIni >= 0:
        break

print()

DifVal = Valfin - ValIni
Perc = (abs(DifVal) / ValIni) * 100

if DifVal < 0:
    print("A Variacao percentual foi de -", Perc, "%")
else:
    print("A Variacao percentual foi de +", Perc, "%")

print()

