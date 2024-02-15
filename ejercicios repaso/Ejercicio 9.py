 #9. Crear un programa que genere una matriz de números y la imprima en pantalla.
def imprimir_matriz(matriz):
    for fila in matriz:
        for j in fila:
            print(j, end=" ")
        print()

matriz_real = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
imprimir_matriz(matriz_real)