print(" MINI QUIZ")
correctas = 0
respuesta1 = input("1. ¿Capital de Guatemala? ")
if respuesta1.lower() == "guatemala":
    correctas = correctas + 1
respuesta2 = input("2. ¿Cuánto es 5 + 3? ")
if respuesta2 == "8":
    correctas = correctas + 1
respuesta3 = input("3. ¿Color del sol? ")
if respuesta3.lower() == "amarillo":
    correctas = correctas + 1

print("Obtuviste", correctas, "de 3 correctas")

if correctas == 3:
    print("¡Perfecto!")
elif correctas == 2:
    print("¡Muy bien!")
elif correctas == 1:
    print("Puedes mejorar")
else:
    print("Sigue estudiando")