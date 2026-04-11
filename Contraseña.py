def tiene_mayuscula(texto):
    for c in texto:
        if c.isupper():
            return True
    return False

def tiene_digito(texto):
    for c in texto:
        if c.isdigit():
            return True
    return False

def tiene_especial(texto):
    especiales = "!@#$%"
    for c in texto:
        if c in especiales:
            return True
    return False

def no_tres_iguales(texto):
    for i in range(len(texto) - 2):
        if texto[i] == texto[i+1] == texto[i+2]:
            return False
    return True

def validar_password(password):
    return (
        len(password) >= 8 and
        tiene_mayuscula(password) and
        tiene_digito(password) and
        tiene_especial(password) and
        no_tres_iguales(password) 
    )

def diagnosticar_password(password):
    if len(password) < 8:
        print(" Mínimo 8 caracteres")
    if not tiene_mayuscula(password):
        print(" Falta una mayúscula")
    if not tiene_digito(password):
        print(" Falta un dígito")
    if not tiene_especial(password):
        print("Falta un carácter especial")
    if not no_tres_iguales(password):
        print("Tiene 3 caracteres iguales seguidos")

diagnosticar_password("MiClaaave1233!")