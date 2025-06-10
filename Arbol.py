# Definimos la clase Persona para representar a cada miembro del árbol genealógico
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre                    # Nombre de la persona
        self.hijo_izquierdo = None             # Referencia al primer hijo (izquierdo)
        self.hijo_derecho = None               # Referencia al segundo hijo (derecho)

# Función para imprimir el árbol genealógico en forma jerárquica
def imprimir_arbol(persona, nivel=0):
    if persona:
        # Imprime el nombre de la persona con indentación según su nivel
        print("  " * nivel + f"- {persona.nombre}")
        # Llama recursivamente para imprimir los hijos (izquierda y derecha)
        imprimir_arbol(persona.hijo_izquierdo, nivel + 1)
        imprimir_arbol(persona.hijo_derecho, nivel + 1)

def buscar_persona(raiz, nombre):
    if raiz is None:
        return None
    if raiz.nombre == nombre:
        return raiz
    izquierda = buscar_persona(raiz.hijo_izquierdo, nombre)
    if izquierda:
        return izquierda
    return buscar_persona(raiz.hijo_derecho, nombre)

# Se pide al usuario que ingrese el nombre del ancestro principal (raíz del árbol)
nombre_raiz = input("Ingrese el nombre del ancestro principal (raíz): ")
raiz = Persona(nombre_raiz)  # Se crea la raíz del árbol


while True:
    print("\nOpciones:")
    print("1. Agregar hijo")
    print("2. Mostrar árbol genealógico")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        # Se ingresan los datos del padre/madre y del nuevo hijo
        padre_nombre = input("Ingrese el nombre del padre/madre: ")
        nuevo_nombre = input("Ingrese el nombre del nuevo hijo/hija: ")

        # Se busca la persona a quien se le quiere agregar un hijo
        padre = buscar_persona(raiz, padre_nombre)
        if padre is None:
            print("❌ Persona no encontrada.")  # No se encontró a esa persona en el árbol
        else:
            # Si se encuentra, se crea el nuevo hijo
            nuevo_hijo = Persona(nuevo_nombre)
            if padre.hijo_izquierdo is None:
                padre.hijo_izquierdo = nuevo_hijo  # Se agrega como hijo izquierdo
                print(f"✅ Hijo agregado a la izquierda de {padre.nombre}.")
            elif padre.hijo_derecho is None:
                padre.hijo_derecho = nuevo_hijo  # Se agrega como hijo derecho
                print(f"✅ Hijo agregado a la derecha de {padre.nombre}.")
            else:
                print("⚠️ Esta persona ya tiene dos hijos.")  # Ya tiene el máximo de hijos permitidos
    elif opcion == "2":
        # Muestra el árbol actual con todos sus miembros
        print("\nÁrbol Genealógico:")
        imprimir_arbol(raiz)

    elif opcion == "3":
        # Finaliza el programa
        print("👋 Saliendo del programa.")
        break
    else:
        # Opción inválida del menú
        print("❌ Opción no válida.")
