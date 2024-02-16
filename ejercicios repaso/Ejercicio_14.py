def main():
    Lista=[1,2,3,4,5,6]
    contador = 0
    suma = 0
    for i in Lista:
        suma = suma + i
        contador +=1
    Media_aritmetica= suma/contador
    print(f"La media aritmetica de la lista: {Lista} es: {Media_aritmetica}")
main()

