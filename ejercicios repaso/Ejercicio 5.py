 #5. Crear una función que convierta grados Fahrenheit a grados Celsius.

def conversion_grados(a):
    celsius = (a - 32) * 5 / 9
    return celsius

temperatura = int(input("Ingrese la temperatura que desea convertir a Celsius: "))
celcius = conversion_grados(temperatura)
print("La conversión da como resultado:", celcius)
