#ESCRIBE UN PROGRAMA QUE TOME UNA LISTA DE NUMEROS Y DEVUELVA SOLO LOS NUMEROS PARES.

numbers = [3,7,4,9,12,13,11,10,18,20,22]

for number in numbers:
    if number % 2 == 0:
        print(number)