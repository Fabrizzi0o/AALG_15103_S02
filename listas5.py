#lista = [ 2*x for x in [1,2,3,4,5,6,7,8,9,10]]
lista = [2 * x for  x in range(1,10+1)]
print(lista)

lista = [x for x in range (1,101) if x%3==0] # el % en programacion hace lo que hace una division normal , es solo su simbolo 
print (lista)