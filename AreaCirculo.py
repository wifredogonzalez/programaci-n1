def area_circulo(r):
    pi = 3.1416
    area = pi * (r ** 2)
    return area

def es_primo (n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n < 0:
        return "No se puede calcular el factorial de un número negativo"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
def fibonacci(n):
    if n < 0:
        return "No se puede calcular el Fibonacci de un número negativo"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def maximo(lista):
    if not lista:
        return "La lista está vacía"
    max_valor = lista[0]
    for num in lista:
        if num > max_valor:
            max_valor = num
    return max_valor


