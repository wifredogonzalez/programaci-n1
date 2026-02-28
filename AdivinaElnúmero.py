import random
numero_secreto = random.randint(1, 100)
intentos = 0
while True: 
    intento = int(input("¿Puedes adivinar el numero (1-100):"))
    intentos += 1
    if intento < numero_secreto:
        print("Más alto")
    elif intento > numero_secreto:
        print("Más bajo")
    else:
        print(f"Correcto en {intentos} intentos, enhorabuena")
    
    if intentos == 7:
        print(f"Se acabó, alcanzó su numero de intentos maximo ({intentos} intentos)")
        break