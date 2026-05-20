num = int(input ("Ingrese numero a buscar : "))
Lista = [1,2,3,4,5,6,7,8,9]
for x in Lista:#Crea un objeto "X" que ejecutara la operacion de buscar en la lista con el codigo de abajo 
    if x== num:
        print ("Encontrado")
else :
    print ("No se ha encontrado este numero")