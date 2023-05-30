def contar_primos(x):
    cont = 0
    rang = range(2,x+1)
    for i in rang:
        if i % 2 == 0:
            cont += 1
    return cont

print(contar_primos(15))

