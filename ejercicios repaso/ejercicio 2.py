# 3. Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random
lista= [random.randint(1, 100) for _ in range(10)]
print("lista de numeros",lista)



