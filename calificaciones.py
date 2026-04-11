def promedio(notas):
    return sum(notas) / len(notas)

def mayor(notas):
    m = notas[0]
    for n in notas:
        if n > m:
            m = n
    return m

def menor(notas):
    m = notas[0]
    for n in notas:
        if n < m:
            m = n
    return m

def contar_aprobados(notas, minimo=61):
    count = 0
    for n in notas:
        if n >= minimo:
            count += 1
    return count

def histograma(notas):
    for n in notas:
        print(f"{n}: {'*' * (n // 5)}")

def reporte(notas):
    print("Promedio:", promedio(notas))
    print("Mayor:", mayor(notas))
    print("Menor:", menor(notas))
    print("Aprobados:", contar_aprobados(notas))
    print("\nHistograma:")
    histograma(notas)


notas = [85, 42, 73, 61, 55, 90, 38, 77, 95, 60]
reporte(notas)