def mostrar_menu():
    print("Seleccione la operación a realizar:")
    print(" +    Suma")
    print(" -    Resta")
    print(" *    Multiplicación")
    print(" /    División")
    print(" ^    Potencia")
    print(" %    Módulo")
    print(" escribir 'salir' para terminar")


def obtener_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")


def calcular(a, b, operacion):
    if operacion == "+":
        return a + b
    if operacion == "-":
        return a - b
    if operacion == "*":
        return a * b
    if operacion == "/":
        if b == 0:
            raise ZeroDivisionError("División por cero")
        return a / b
    if operacion == "^":
        return a ** b
    if operacion == "%":
        if b == 0:
            raise ZeroDivisionError("Módulo por cero")
        return a % b
    raise ValueError("Operación no soportada")


def main():
    while True:
        mostrar_menu()
        operacion = input("Ingrese el símbolo de la operación (o 'salir'): ").strip()
        if operacion.lower() in ("salir", "q", "exit"):
            print("Saliendo...")
            break
        if operacion not in ("+", "-", "*", "/", "^", "%"):
            print("Operación no válida. Intente de nuevo.")
            continue
        a = obtener_numero("Ingrese el primer número: ")
        b = obtener_numero("Ingrese el segundo número jajaja: ")
        try:
            resultado = calcular(a, b, operacion)
        except ZeroDivisionError as e:
            print("Error:", e)
            continue
        except Exception as e:
            print("Error:", e)
            continue
        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
print ("la mejor calculadora del mundo")
print( "practica commit")
("ignora esto")
