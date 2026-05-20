"""
Cree una clase Persona en python con los atributos nombre y DNI, y cree un aplicativo con un menú con tres opciones:
1. Crear persona, donde pedirá los datos y creará una persona y la agregará a la lista.
2. Listar, donde mostrará todas las personas que hay en la lista.
3. Eliminar, donde pedirá un DNI y borrará a la persona que tenga ese DNI de la lista.
Habrá también una cuarta opción, que es Salir.
"""
# =====================================================================
# 1. DEFINICIÓN DE LA CLASE (El molde)
# =====================================================================
class Persona: 

    # 📌 ESTE ES EL CONSTRUCTOR
    # Se ejecuta automáticamente CADA VEZ que creas una nueva persona.
    # Sirve para darle los datos iniciales (nombre y dni) al objeto.
    def __init__(self, nombre, dni): 
        self.nombre = nombre   # Atributo: guarda el nombre de la persona
        self.dni = dni         # Atributo: guarda el DNI de la persona

    # 📌 ESTE ES UN MÉTODO (Una función propia de la clase)
    # Es una acción que los objetos del tipo "Persona" saben hacer.
    # En este caso, sabe armar un texto con sus propios datos.
    def mostrar(self): 
        return f"Nombre: {self.nombre} | DNI: {self.dni}" 


# =====================================================================
# 2. EL PROGRAMA PRINCIPAL (Fuera de la clase)
# =====================================================================

# Lista vacía donde guardaremos todas las personas que creemos
personas = [] 

# Ciclo infinito para mostrar el menú interactivamente
while True: 
    print("\n--- MENÚ ---")
    print("1. Crear persona") 
    print("2. Listar personas") 
    print("3. Eliminar persona") 
    print("4. Salir") 
    
    opcion = input("Seleccione una opción: ") 
    
    # -----------------------------------------------------------------
    # OPCIÓN 1: Aquí usamos el "Constructor"
    # -----------------------------------------------------------------
    if opcion == "1": 
        nombre = input("Ingrese nombre: ") 
        dni = input("Ingrese DNI: ") 
        
        # 🔑 AQUÍ LLAMAS AL CONSTRUCTOR: 'Persona(nombre, dni)' activa el __init__
        nueva_persona = Persona(nombre, dni) 
        
        # Agregamos el objeto recién creado a nuestra lista
        personas.append(nueva_persona) 
        print("Persona agregada correctamente.")
        
    # -----------------------------------------------------------------
    # OPCIÓN 2: Aquí usamos el "Método" para ver los datos
    # -----------------------------------------------------------------
    elif opcion == "2": 
        if not personas:
            print("No hay personas registradas.") 
        else: 
            for persona in personas: 
                # 🔑 AQUÍ USAS EL MÉTODO: 'persona.mostrar()' pide los datos formateados
                print(persona.mostrar())
                
    # -----------------------------------------------------------------
    # OPCIÓN 3: Eliminar buscando por DNI
    # -----------------------------------------------------------------
    elif opcion == "3": 
        dni_buscar = input("Ingrese DNI a eliminar: ") 
        eliminado = False 
        
        for persona in personas: 
            # Compara el DNI que ingresaste con el atributo .dni de cada objeto
            if persona.dni == dni_buscar: 
                personas.remove(persona) # Lo saca de la lista
                eliminado = True 
                print("Persona eliminada.") 
                break # Rompe el for para dejar de buscar
                
        if not eliminado: 
            print("No se encontró ese DNI.") 
            
    # -----------------------------------------------------------------
    # OPCIÓN 4: Salir del ciclo
    # -----------------------------------------------------------------
    elif opcion == "4": 
        print("Saliendo del programa...") 
        break # Rompe el 'while True' y el programa termina
        
    else: 
        print("Opción inválida.")