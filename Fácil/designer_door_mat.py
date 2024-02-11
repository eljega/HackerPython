"""
El señor Vincent trabaja en una compañía que fabrica felpudos. Un día, diseñó un nuevo felpudo con las siguientes especificaciones:

El tamaño del felpudo debe ser N x M (N es un número natural impar y M es 3 veces N).
El diseño debe tener la palabra 'WELCOME' escrita en el centro.
El patrón del diseño debe usar únicamente los caracteres '|', '.' y '-'.
Diseños de Muestra

    Tamaño: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Tamaño: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Formato de Entrada

Una línea única que contiene los valores de N y M separados por un espacio.

Restricciones

Formato de Salida

Producir el patrón de diseño.

Entrada de Muestra

9 27
Salida de Muestra

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

# solicitamos al usuario que ingrese los valores de n y m.
N, M = map(int, input("Ingrese los valores de N y M separados por un espacio: ").split())

# generamos la parte superior
for i in range(1, N, 2): 
    print(('.|.' * i).center(M, '-'))

# generamos la parte central con el texto 'WELCOME'
print('WELCOME'.center(M, '-'))

# y la parte inferior del diseño
for i in range(N-2, -1, -2):
    print(('.|.' * i).center(M, '-'))