#15. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    if cadena == cadena[::-1]:
        return True
    else:
        return False

entrada_usuario = input("Ingresa una palabra o frase: ")

if es_palindromo(entrada_usuario):
    print("El texto ingresado  es un palíndromo")
else:
    print("El texto ingresado no es un palíndromo")
