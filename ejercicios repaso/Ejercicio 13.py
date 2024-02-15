#13. Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división.

def suma(num_1,num_2):
    return num_1 + num_2
def resta(num_1,num_2):
    return num_1-num_2
def multiplicar(num_1,num_2):
    return num_1*num_2
def dividir(dividendo, divisor):
    if divisor != 0:  # Verificar que el divisor no sea cero
        resultado = dividendo / divisor
        return resultado
    else:
        return "Error: No se puede dividir por cero"

numero1=int(input("ingrese el primer numero"))
numero2=int(input("ingrese el segundo numero"))

sumar=suma(numero1,numero2)
restar=resta(numero1,numero2)
multiplicacion=multiplicar(numero1,numero2)
division=dividir(numero1,numero2)

print("los resultados con los 2 numeros son: suma= ",sumar,"resta= ",restar,"multiplicacion=",multiplicacion, "y division= ",division)