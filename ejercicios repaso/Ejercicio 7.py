#7. Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.
def encontrar_extremos(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

numeros = [15, 55, 7, 22, 14, 1,100,99,0]
maximo, minimo = encontrar_extremos(numeros)
print("El número más grande es:", maximo)
print("El número más pequeño es:", minimo)