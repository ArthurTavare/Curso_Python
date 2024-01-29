nomes = ["Gabriel" , "Danny" , "Arthur" , "Joao", "lucas"]
# novalista = []
#for x in nomes:
#    if "u" in x:
#        novalista.append(x)

# novalista = [x for x in nomes if x != "Danny" ]
# novalista = [x for x in nomes if "u" in x]
# novalista = [x for x in nomes ]
# novalista = [x for x in range (10) if  x % 2 == 0]
# novalista = [x.upper() for x in nomes ]
novalista = [x if x != "Danny" else "Danielle" for x in nomes ]



print(novalista)