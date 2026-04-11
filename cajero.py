def calcular_billetes(monto):
    if monto % 5 != 0:
        print("Error: el monto debe ser múltiplo de 5.")
        return None

    bQ200 = monto // 200
    monto = monto % 200

    bQ100 = monto // 100
    monto = monto % 100

    bQ50 = monto // 50
    monto = monto % 50

    bQ20 = monto // 20

    bQ10 = monto // 10
    monto = monto % 10

    bQ5 = monto // 5


    return f"{bQ200}x Q200, {bQ100}x Q100, {bQ50}x Q50, {bQ20}x Q20, {bQ10}x Q10, {bQ5}x Q5"

print(calcular_billetes(370))

    