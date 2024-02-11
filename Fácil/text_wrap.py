"""
Nombre de el ejercicio: Text Wrap

Dificultad: Fácil

Instrucciones del Ejercicio:

Se te da una cadena de texto y un ancho (width). 
Tu tarea es envolver la cadena en un párrafo con el ancho dado.

Descripción de la Función:

Completa la función wrap en el editor abajo.

La función wrap tiene los siguientes parámetros:

string string: una cadena larga de texto.
int max_width: el ancho al que se debe envolver el texto.
Devuelve:

string: una única cadena con caracteres de nueva línea ('\n') donde deberían ir los saltos de línea.
Formato de Entrada:

La primera línea contiene la cadena de texto, string.
La segunda línea contiene el ancho, max_width.

Restricciones:

Se asume que 'max_width' es un entero positivo y que 'string' es una cadena no vacía.

Ejemplo de Entrada 0:

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Ejemplo de Salida 0:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

"""

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    #  Obtener la cadena de texto y el ancho máximo de línea.
    string, max_width = input("Ingrese la cadena de texto a envolver: "), int(input("Ingrese el ancho máximo de línea: "))
    # Obtener el resultado de la funcion wrap.
    result = wrap(string, max_width)
    print(result)
