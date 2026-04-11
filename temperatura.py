def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def celsius_a_kelvin(c):
    return c + 273.15

def celsius_a_rankine(c):
    return (c + 273.15) * 9/5

def convertir(valor, origen, destino):
    origen = origen.upper()
    destino = destino.upper()

    if origen == destino:
        return valor


    if origen == "F":
        valor = fahrenheit_a_celsius(valor)
    elif origen == "K":
        valor = valor - 273.15
    elif origen == "R":
        valor = (valor - 491.67) * 5/9
    elif origen != "C":
        return None

    # convertir desde Celsius
    if destino == "C":
        return valor
    elif destino == "F":
        return celsius_a_fahrenheit(valor)
    elif destino == "K":
        return celsius_a_kelvin(valor)
    elif destino == "R":
        return celsius_a_rankine(valor)

    return None

print(convertir(0, "C", "F"))
print(convertir(32, "F", "C"))  
print(convertir(0, "C", "K"))   
print(convertir(300, "K", "C")) 