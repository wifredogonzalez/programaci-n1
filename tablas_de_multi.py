def tabla(n, hasta=10): 
    for i in range(1, hasta + 1):
        print(f"{n} x {i} = {n*i}")

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tablas_primos(limite):
    for i in range(2, limite + 1):
        if es_primo(i):
            print(f"\nTabla del {i}:")
            tabla(i)