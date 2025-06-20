# Función que crea una persona representada como un diccionario 
def crear_persona(nombre):
    return {
        "nombre": nombre.lower(),         # Guarda el nombre en minúsculas para mantener uniformidad
        "hijo_izquierdo": None,           # Inicialmente no tiene hijo izquierdo
        "hijo_derecho": None              # Inicialmente no tiene hijo derecho
    }

# Función recursiva para imprimir el árbol genealógico de manera jerárquica
def imprimir_arbol(persona, nivel=0):
    if persona:
        # Imprime el nombre con una indentación proporcional al nivel en el árbol
        print("  " * nivel + f"- {persona['nombre']}")
        # Llama recursivamente para imprimir el hijo izquierdo
        imprimir_arbol(persona["hijo_izquierdo"], nivel + 1)
        # Llama recursivamente para imprimir el hijo derecho
        imprimir_arbol(persona["hijo_derecho"], nivel + 1)

# Función para buscar a una persona en el árbol por su nombre
def buscar_persona(raiz, nombre):
    if raiz is None:
        return None  # Si el nodo actual está vacío, termina búsqueda
    if raiz["nombre"] == nombre.lower():
        return raiz  # Si el nombre coincide (en minúsculas), se devuelve
    # Busca recursivamente en el hijo izquierdo
    izquierda = buscar_persona(raiz["hijo_izquierdo"], nombre)
    if izquierda:
        return izquierda  # Si se encuentra en la izquierda, se devuelve
    # Si no se encontró en la izquierda, busca en la derecha
    return buscar_persona(raiz["hijo_derecho"], nombre)

# Recorrido INORDEN: primero el hijo izquierdo, luego la persona, luego el derecho
def recorrido_inorden(persona):
    if persona:
        recorrido_inorden(persona["hijo_izquierdo"])
        print(persona["nombre"])  # Visita el nodo actual
        recorrido_inorden(persona["hijo_derecho"])

# Recorrido PREORDEN: primero la persona, luego izquierda, luego derecha
def recorrido_preorden(persona):
    if persona:
        print(persona["nombre"])  # Visita el nodo actual
        recorrido_preorden(persona["hijo_izquierdo"])
        recorrido_preorden(persona["hijo_derecho"])

# Recorrido POSTORDEN: primero los hijos, luego la persona
def recorrido_postorden(persona):
    if persona:
        recorrido_postorden(persona["hijo_izquierdo"])
        recorrido_postorden(persona["hijo_derecho"])
        print(persona["nombre"])  # Visita el nodo actual

# Solicita al usuario el nombre del ancestro principal del árbol
nombre_raiz = input("Ingrese el nombre del ancestro principal (raíz): ")
raiz = crear_persona(nombre_raiz)  # Crea la raíz del árbol

# Bucle principal del programa con menú interactivo
while True:
    # Muestra las opciones disponibles
    print("\nOpciones:")
    print("1. Agregar hijo")
    print("2. Mostrar árbol genealógico")
    print("3. Recorrido INORDEN")
    print("4. Recorrido PREORDEN")
    print("5. Recorrido POSTORDEN")
    print("6. Salir")

    # Lee la opción elegida por el usuario
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Solicita los nombres del padre/madre y del nuevo hijo/hija
        padre_nombre = input("Ingrese el nombre del padre/madre: ")
        nuevo_nombre = input("Ingrese el nombre del nuevo hijo/hija: ")

        # Busca a la persona correspondiente al padre/madre
        padre = buscar_persona(raiz, padre_nombre)
        if padre is None:
            print("Persona no encontrada.")  # Si no existe, muestra mensaje de error
        else:
            nuevo_hijo = crear_persona(nuevo_nombre)  # Crea el nuevo hijo
            # Intenta agregarlo como hijo izquierdo si está vacío
            if padre["hijo_izquierdo"] is None:
                padre["hijo_izquierdo"] = nuevo_hijo
                print(f"Hijo agregado a la izquierda de {padre['nombre']}.")
            # Si no, intenta como hijo derecho
            elif padre["hijo_derecho"] is None:
                padre["hijo_derecho"] = nuevo_hijo
                print(f"Hijo agregado a la derecha de {padre['nombre']}.")
            # Si ya tiene dos hijos, no se puede agregar más
            else:
                print("Esta persona ya tiene dos hijos.")

    elif opcion == "2":
        # Imprime el árbol completo en formato jerárquico
        print("\nÁrbol Genealógico:")
        imprimir_arbol(raiz)

    elif opcion == "3":
        # Muestra los nombres en recorrido INORDEN
        print("\nRecorrido INORDEN:")
        recorrido_inorden(raiz)

    elif opcion == "4":
        # Muestra los nombres en recorrido PREORDEN
        print("\nRecorrido PREORDEN:")
        recorrido_preorden(raiz)

    elif opcion == "5":
        # Muestra los nombres en recorrido POSTORDEN
        print("\nRecorrido POSTORDEN:")
        recorrido_postorden(raiz)

    elif opcion == "6":
        # Finaliza el programa
        print("Saliendo del programa.")
        break

    else:
        # Si la opción ingresada no es válida
        print("Opción no válida.")