def main():
    numero = int(input("Ingrese un numero:"))
    factorial = 1
    for i in range(1,numero+1):
        factorial=factorial*i
    print(f"El factorial del número {numero} es: {factorial}")
main()