def busqueda_binaria(lista, objetivo):
    
    """Devuelve el índice de 'objetivo' en 'lista' o -1 si no se encuentra."""
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
buscar =2
resultado = busqueda_binaria(numeros, buscar) 
if resultado != -1: 
    print(f"Número encontrado en la posición {resultado}") 
else: print("Número no encontrado")