# Escribe un programa que pida al usuario ingresar su edad y luego imprima un mensaje indicando si es mayor de edad o no.

while True:
    edad = int(input("Ingrese su edad: "))

    if edad >= 18:
        print("SOS MAYOR DE EDAD!!")
    else:
        print("SOS MENOR DE EDAD!!")
    
    opt = input("Desea ingresar otra edad?? (s/n)\n")
    if opt.lower() != 's':
        break
