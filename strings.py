edad = 20
#c#
#Console.WriteLine($"Tengo {edad} años\n");
#Console.WriteLine(@"Tengo {edad} años\n");
#FUNCIONES DE MANIPULACION DE TEXTO
#python
print(f"Tengo {edad} años\n");#la f activa las llaves 
print(r"Tengo {edad} años\n");#la r hace todo en crudo , agrrar literalmente {edad} y no hara el salto de linea , copiara todo como tal esta 

a = "carlos 20 105148464 interbank"
b = "carlos|20|105148464|interbank"
print(a.split()) #pone toda la informacion en unos corchetes
c=b.split("|")#elimina cada | que encuentre en la lista 
print(c)
d="@".join(c)
print(d)

spam = 'SpamSpamBaconSpamEggsSpamSpam'
z=spam.strip('Spam')#esto elimina lo que le diga de "spam"
print(z)