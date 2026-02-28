print("Bienvenido a Banco Gonzalez")
pin = int(input("Ingrese su PIN:"))
if pin == 1234:
    print("Acceso concedido")
else:
    print("PIN incorrecto")
monto= float(input("ingrese monto a retirar:"))
if pin == 1234 and monto > 0 and monto <= 5000:
        print(f"Retiro realizado correctamente {monto}")
else:
    print("Monto no válido, debe de ser mayor a 5000")