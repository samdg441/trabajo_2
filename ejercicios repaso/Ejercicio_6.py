def main():
    Lista = []
    stop = 1
    suma = 0
    while stop != 0:
        numero = int(input("Ingrese un número diferente de 0 o digite 0 para terminar:"))
        if numero == 0:
            break
        else:
            Lista.append(numero)
    for i in Lista:
        suma = suma + i
    print(Lista)
    print(f"La suma total de los numeros ingresados en la lista es: {suma}")
main()