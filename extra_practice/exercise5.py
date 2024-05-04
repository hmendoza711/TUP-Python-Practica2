#ESCRIBE UN PROGRAMA QUE TOME DOS TUPLAS E IMPRIMA UN DICCIONARIO DONDE LAS PRIMERAS TUPLAS SEAN LAS CLAVES Y LAS SEGUNDAS TUPLAS SEAN LOS VALORES CORRESPONDIENTES.

tuple_keys = ('Nombre','Apellido','Dni','Direccion')
tuple_values = ('Héctor','Mendoza',37582287,'Mitre 929')

dictionary = dict(zip(tuple_keys,tuple_values))

print(dictionary)
