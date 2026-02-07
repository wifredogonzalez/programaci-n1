from calculadora import calcular

tests = [
    (2, 3, "+", 5),
    (5, 2, "-", 3),
    (4, 3, "*", 12),
    (8, 2, "/", 4),
    (2, 3, "^", 8),
    (7, 3, "%", 1),
]

for a, b, op, expected in tests:
    result = calcular(a, b, op)
    print(f"{a} {op} {b} = {result} (esperado {expected})")

# prueba de división por cero
try:
    calcular(1, 0, "/")
except ZeroDivisionError as e:
    print("Capturada excepción esperada:", e)
