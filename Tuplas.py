lat,lon = mi_coordenada = ("14.30575","-90.77400")
def analizar_numeros(lista):
    minimo = min(lista)
    maximo = max(lista)
    promedio = sum(lista) / len(lista)
    
    return (minimo, maximo, promedio)
numeros = [10, 5, 8, 20, 15]

resultado = analizar_numeros(numeros)

print(resultado)

#Al modificar un elemento de la tupla tira TypeError: 'tuple' object does not support item assignment