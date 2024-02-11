"""
Nombre de el ejercicio: Text Alignment

Dificultad: Fácil

Instrucciones del Ejercicio:

En Python, una cadena de texto se puede alinear a la izquierda, al centro y a la derecha utilizando los métodos .ljust(width), .center(width) y .rjust(width).

.ljust(width):
Este método devuelve una cadena alineada a la izquierda de longitud 'width'.
Ejemplo:
    width = 20
    print('HackerRank'.ljust(width, '-'))
Salida:
    HackerRank----------

.center(width):
Este método devuelve una cadena centrada de longitud 'width'.
Ejemplo:
    width = 20
    print('HackerRank'.center(width, '-'))
Salida:
    -----HackerRank-----

.rjust(width):
Este método devuelve una cadena alineada a la derecha de longitud 'width'.
Ejemplo:
    width = 20
    print('HackerRank'.rjust(width, '-'))
Salida:
    ----------HackerRank

Tarea:
Se te proporciona un código parcial que se utiliza para generar el logotipo de HackerRank con un grosor variable. Tu tarea es reemplazar los espacios en blanco (______) con rjust, ljust o center para obtener el logotipo deseado.

Formato de Entrada:
Una sola línea que contiene el valor del grosor para el logotipo.

Restricciones:
El grosor debe ser un número impar.

Formato de Salida:
Produce el logotipo deseado.

Salida Esperada:
La salida debe ser el logotipo de HackerRank con el grosor proporcionado, siguiendo el patrón específico que incluye un cono superior, pilares superiores e inferiores, un cinturón medio y un cono inferior invertido.

Ejemplo de Salida para un grosor de 5:
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
HHHHHHHHHHHHHHHHHHHHHHHHHHH   
HHHHHHHHHHHHHHHHHHHHHHHHHHH   
HHHHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
          HHHHHHHHH           
           HHHHHHH            
            HHHHH             
             HHH              
              H               
"""


thickness = int(input("Ingrese el grosor del logo con un (numero impar): ")) # esto debe ser un numero impar
c = 'H'

# parte superior
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# pilares superiores
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# medio
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

# pilares inferiores
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# parte inferior
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
