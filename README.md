# Trabajo práctico integrador de programación 1
# Árbol Genealógico en Python

Profesores:Bruselario Sebastián, Nicolás Quirós

Tutores: Gubiotti Florencia, Neyén Bianchi

Alumnos: Rocio Santarelli comisión 9, Yoel Santarelli comisión 21.

Link del video: [Trabajo practico integrador Programación 1](https://youtu.be/gFoT_QnMEm0)

Este proyecto es una aplicación simple de consola desarrollada en Python que permite construir e imprimir un árbol genealógico. Los usuarios pueden agregar hasta dos hijos por persona y visualizar la estructura familiar de manera jerárquica.

# Funcionalidades

- Crear un árbol genealógico iniciando desde un ancestro raíz.
- Agregar hijos a una persona existente (máximo dos hijos: izquierdo y derecho).
- Imprimir el árbol genealógico en un formato jerárquico.
- Interfaz de menú interactivo desde la terminal.

# Requisitos Técnicos

- Python 3 instalado
- No requiere librerías externas

# Cómo usar

1. Cloná este repositorio o descargá el archivo `Arbol.py`:
   ```bash
   git clone https://github.com/GYoelSantarelli/TP-Integrador-P1
   cd TP-Integrador-P1
# Como usar el programa paso a paso

1. Ejecutar el archivo
   ```bash
   python Arbol.py
2. Ingresar el ancestro raíz
   Al iniciar el programa se te solicita ingresar el nombre del ancestro principal, es decir la primer persona del árbol genealógico
   Ingrese el nombre del ancestro principal (raíz): Juan.
3. Usar el menú interactivo
   Despues de ingresar el nombre del ancestro aparecerá un menú

   Opciones:
   1. Agregar hijo
   2. Mostrar árbol genealógico
   3. Recorrido INORDEN
   4. Recorrido PREORDEN
   5. Recorrido POSTORDEN
   6. Salir
   Seleccione una opción:

   Si seleccionas la opción 1, lo que harás es agregar un hijo y te pedirá que ingreses
   - El nombre del padre o madre al que le querés agregar un hijo.
   - El nombre del nuevo hijo o hija.
   ```bash
   Ingrese el nombre del padre/madre: Juan
   Ingrese el nombre del nuevo hijo/hija: Ana
   ```
   - Si la persona que ingresaste, aún no tiene asignado ningún hijo, el nuevo hijo se agregará como hijo izquierdo
   - Si ya tiene un hijo izquierdo, el nuevo se agregará como hijo derecho.
   - Y si ya tiene dos hijos, se mostrar el mensaje: Esta persona ya tiene dos hijos.

   Si seleccionas la opción 2, lo que hará el programa es mostrarte el árbol genealógico en el momento actual de forma jerarquica. Por ejemplo:
   Árbol Genealógico:
   - Juan (Jerarquía 0)
     - Ana (Jerarquía 1)
     - Pedro (Jerarquía 1)
       - Sofía (Jerarquía 2)
   
   Eligiendo la opción 3, lo que hará el programa es mostrarte en el momento actual el recorrido de forma INORDEN

   Eligiendo la opción 4, lo que hará el programa es mostrarte en el momento actual el recorrido de forma PREORDEN

   Eligiendo la opción 5, lo que hará el programa es mostrarte en el momento actual el recorrido de forma POSTORDEN

   Eligiendo la opción 6, el programa finaliza y te muestra el siguiente mensaje: Saliendo del programa.
  # Notas
- El programa está diseñado para funcionar como un árbol binario, por lo que cada persona puede tener como máximo dos hijos.

- Los nombres se comparan literalmente, por lo que debés escribirlos exactamente igual al agregarlos o buscarlos.

- Podés usar el programa tantas veces como quieras agregando nuevos hijos y explorando el árbol.
