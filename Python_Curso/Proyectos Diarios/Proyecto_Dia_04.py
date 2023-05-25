from random import *

nombre = input('Tú nombre: ')
print(f'{nombre} piensa un número del 1 al 100 y tienes solo 8 intentos para adivinarlo')
valor = randint(1,100)
numero = 0

for i in range(1,9):
    numero = int(input("Di un número: "))
    if numero > 100 or numero <= 0:
        print("Este número no está permitido")
    elif numero < valor:
        print("respueta incorrecta es menor al valor")
    elif numero > valor:
        print("respueta incorrecta es mayor al valor")
    else:
        print(f"Enhorabuena lo has adivinado, en {i} intentos")
        break

if numero != valor:
    print("Fin del Juego vuelve a intentarlo")