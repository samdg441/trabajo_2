#11. Crear un programa que genere una lista de números pares entre 1 y 100.
lista_pares=list(range(1,101))

for lista_pares in lista_pares:
    if lista_pares % 2 == 0:
        print(lista_pares)