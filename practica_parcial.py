#int = enteros nombre = int(input(":"))
#float = decimales
#str = cadenas de texto 
#bool = booleanos (verdadero o falso)
#f-string = permite insertar variables dentro de una cadena de texto
nombre = "Wilfredo"
print(f"Hola {nombre}")
#+ = suma
#- = resta  
#* = multiplicacion
#/ = division
#% = modulo (resto de una division)
#** = potencia
#// = division entera (devuelve el cociente sin el resto)
# if/elif/else
edad = int(input("Edad: "))

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
#match/case
dia = input("Ingresa día: ")

match dia:
    case "lunes":
        print("Inicio de semana")
    case "viernes":
        print("Fin de semana laboral")
    case _:
        print("Día normal")
#validacion de inputs
# .isdigit() = verifica si una cadena es un número entero
if numero.isdigit():
    numero = int(numero)
# .isalpha() = verifica si una cadena es solo letras
nombre = input("Nombre: ")

if nombre.isalpha():
    print("Solo letras")
#len() = devuelve la longitud de una cadena
password = input("Clave: ")

if len(password) >= 8:
    print("Clave válida")

