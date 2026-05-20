a = [1, 2, 3, 4]
#agregar
a.append(5)#este comando agrega un numero al final de la lista
print(a)

a.insert(1,7)#este comando agrega un numero pero se tiene que aclarar su posicion , se pone primero su ubicacion y luego el numero que se va a agregar 
print(a)
#borrar
a.remove(7)#este comando borra el contenido directamente , puse 7 asi que borrara el numero 7 
print(a)

del a[3] #este comando borra por posicion , en este caso la posicion 3 le pertenece al numero 4
print(a)

#Posicion de algo 

print(a.index(5))#muestra la posicion en la tabla , en este caso el numero 5 esta en la columna numero 3