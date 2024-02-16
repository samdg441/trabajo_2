import math
def main():
    Radio = int(input("Ingrese el radio del circulo:"))
    Area_circulo = Area(Radio)
    print(f"El area del circulo con radio {Radio} es igual a {round(Area_circulo,2)}")
def Area(R):
    radio=R**2
    return math.pi*radio
main()