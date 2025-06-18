def crear_persona(nombre):
    return {
        "nombre": nombre.upper(),
        "hijo_izquierdo": None,
        "hijo_derecho": None
    }

def imprimir_arbol(persona, nivel=0):
    if persona:
        print("  " * nivel + f"- {persona['nombre']}")
        imprimir_arbol(persona["hijo_izquierdo"], nivel + 1)
        imprimir_arbol(persona["hijo_derecho"], nivel + 1)

def buscar_persona(raiz, nombre):
    if raiz is None:
        return None
    if raiz["nombre"] == nombre.upper():
        return raiz
    izquierda = buscar_persona(raiz["hijo_izquierdo"], nombre)
    if izquierda:
        return izquierda
    return buscar_persona(raiz["hijo_derecho"], nombre)

# Se pide al usuario que ingrese el nombre del ancestro principal (raíz del árbol)
nombre_raiz = input("Ingrese el nombre del ancestro principal (raíz): ")
raiz = crear_persona(nombre_raiz)

while True:
    print("\nOpciones:")
    print("1. Agregar hijo")
    print("2. Mostrar árbol genealógico")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        padre_nombre = input("Ingrese el nombre del padre/madre: ")
        nuevo_nombre = input("Ingrese el nombre del nuevo hijo/hija: ")

        padre = buscar_persona(raiz, padre_nombre)
        if padre is None:
            print("Persona no encontrada.")
        else:
            nuevo_hijo = crear_persona(nuevo_nombre)
            if padre["hijo_izquierdo"] is None:
                padre["hijo_izquierdo"] = nuevo_hijo
                print(f"Hijo agregado a la izquierda de {padre['nombre']}.")
            elif padre["hijo_derecho"] is None:
                padre["hijo_derecho"] = nuevo_hijo
                print(f"Hijo agregado a la derecha de {padre['nombre']}.")
            else:
                print("Esta persona ya tiene dos hijos.")
    elif opcion == "2":
        print("\nÁrbol Genealógico:")
        imprimir_arbol(raiz)
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida.")