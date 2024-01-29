# igual a: a == b
# Diferente de: a!= b
# Menor que: a< b
# menor ou igual a: a <= b
# maior que: a > b
# maior ou igual a: a>= b

a = 50
b = 200

if b < a:
    print("b é maior do que a")
    print("outra instrucao no if")
elif a != b:  
     print("a é igual a b")  
elif a + 150 != b:  
     print("a é diferente de b")  
else:
    print("Todas as verificaçaoes retornam false")     


print("Fim do programa")