"""
Dado un entero, n, imprime los siguientes valores para cada entero i desde 1 hasta n:

Decimal
Octal
Hexadecimal (en mayúsculas)
Binario

Descripción de la Función:

Completa la función print_formatted en el editor a continuación.

La función print_formatted tiene los siguientes parámetros:

int number: el valor máximo para imprimir.
Imprime:

Los cuatro valores deben imprimirse en una sola línea en el orden especificado arriba para cada i desde 1 hasta n.
Cada valor debe tener espacios añadidos para coincidir con el ancho del valor binario de n y los valores deben estar separados por un solo espacio.

Formato de Entrada:

Un solo entero que denota n.

Restricciones:

Sample Input:

17
Sample Output:

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
"""

def print_formatted(number):
    width = len("{:b}".format(number))

    for i in range(1, number + 1):
        decimal = str(i)
        octal = "{:o}".format(i)
        hexadecimal = "{:X}".format(i)
        binary = "{:b}".format(i)

        print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")

if __name__ == '__main__':
    n = int(input("Ingrese un número entero:")) # en el ejemplo de HackerRank es 17
    print_formatted(n)
