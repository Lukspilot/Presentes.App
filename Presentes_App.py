#Arranque
from os import system
system("cls")
#import time
print("Hola, bienvenido!")
#time.sleep(1)
system("cls")

#Menu opciones 
while True:
    print("Menú de opciones:")
    print(" ")
    print("1. Ver lista de camilleros")
    print("2. Buscar por apellido")
    print(" ")#Salto de linea

    opcion = int(input("Elija una opción: "))

#Menu opciones 1
    if opcion == 1:
        system("cls")

        print("3. Silva Alex")
        print("4. Garcia Lucas")
        print("5. Aguirre Emiliano")
        print("6. Hernandez Lucas")
        print("7. Coria Carlos")
        print("8. Rosales Leandro")
        print("9. Porres Lucas")
        print("10. <-Regresar al menú anterior")
        print("11. ->Finalizar programa")
        print(" ")#Salto de linea
        opcion = int(input("Elija una opción: "))

        if opcion == 3:
            system("cls")
            print("Los francos de Silva Alex son:")
            print("MARZO")
            francos_Alex = ("Dia → 1", "Dia → 2", "Dia → 3", "Dia → 4", "Dia → 5", "Dia → 6", "Dia → 7", "Dia → 8")
            for elemento in francos_Alex:
                print(elemento)

        if opcion == 4:
            system("cls")
            print("Los francos de Garcia Lucas son:")
            print("MARZO")
            francos_LucasG = ("Dia → 1", "Dia → 2", "Dia → 3", "Dia → 4", "Dia → 5", "Dia → 6", "Dia → 7", "Dia → 8")
            for elemento in francos_LucasG:
                print(elemento)

        if opcion == 5:
            system("cls")
            print("Los francos de Aguirre Emiliano son:")
            print("MARZO")
            francos_Emiliano = ("Dia → 1", "Dia → 2", "Dia → 3", "Dia → 4", "Dia → 5", "Dia → 6", "Dia → 7", "Dia → 8")
            for elemento in francos_Emiliano:
                print(elemento)

        if opcion == 6:
            system("cls")
            print("Los francos de Hernandez Lucas son:")
            print("MARZO")
            francos_LucasH = ("Dia → 1", "Dia → 2", "Dia → 3", "Dia → 4", "Dia → 5", "Dia → 6", "Dia → 7", "Dia → 8")
            for elemento in francos_LucasH:
                print(elemento)

        if opcion == 7:
            system("cls")
            print("Los francos de Coria Carlos son:")
            print("MARZO")
            francos_Carlos = ("Dia → 1", "Dia → 2", "Dia → 3", "Dia → 4", "Dia → 5", "Dia → 6", "Dia → 7", "Dia → 8")
            for elemento in francos_Carlos:
                print(elemento)

        if opcion == 8:
            system("cls")
            print("Los francos de Rosales Leandro son:")
            print("MARZO")
            francos_Leandro = ("Dia → 1", "Dia → 2", "Dia → 3", "Dia → 4", "Dia → 5", "Dia → 6", "Dia → 7", "Dia → 8")
            for elemento in francos_Leandro:
                print(elemento)

        if opcion == 9:
            system("cls")
            print("Los francos de Porres Lucas son:")
            print("MARZO")
            francos_LucasP = ("Dia → 1", "Dia → 2", "Dia → 3", "Dia → 4", "Dia → 5", "Dia → 6", "Dia → 7", "Dia → 8")
            for elemento in francos_LucasP:
                print(elemento)

        if opcion == 10:
            system("cls")
            continue

        if opcion == 11:
            system("cls")
            print("Fin del programa")
            break
#Menu opciones 2
    elif opcion == 2:
        system("cls")
        apellido =str(input("Ingrese apellido del camillero: "))

        if apellido.lower() == "silva":
            print("Los francos de Silva Alex son:")
            print("MARZO")
            francos_Alex = ("Dia → 1", "Dia → 2", "Dia → 3", "Dia → 4", "Dia → 5", "Dia → 6", "Dia → 7", "Dia → 8")
            for elemento in francos_Alex:
                print(elemento)
            print(" ")

        elif apellido.lower() == "garcia":
            print("Los francos de Garcia son:")
            print("MARZO")
            francos_Lucas_G = ("Dia → 1", "Dia → 2", "Dia → 3", "Dia → 4", "Dia → 5", "Dia → 6", "Dia → 7", "Dia → 8")
            for elemento in francos_Lucas_G:
                print(elemento)
            print(" ")

        elif apellido.lower() == "aguirre":
            print("Los francos de Aguirre  son:")
            print("MARZO")
            francos_Aguirre = ("Dia → 1", "Dia → 2", "Dia → 3", "Dia → 4", "Dia → 5", "Dia → 6", "Dia → 7", "Dia → 8")
            for elemento in francos_Aguirre:
                print(elemento)
            print(" ")

        elif apellido.lower() == "hernandez":
            print("Los francos de Hernandez  son:")
            print("MARZO")
            francos_Hernandez = ("Dia → 1", "Dia → 2", "Dia → 3", "Dia → 4", "Dia → 5", "Dia → 6", "Dia → 7", "Dia → 8")
            for elemento in francos_Hernandez:
                print(elemento)
            print(" ")

        elif apellido.lower() == "coria":
            print("Los francos de Coria  son:")
            print("MARZO")
            francos_Coria = ("Dia → 1", "Dia → 2", "Dia → 3", "Dia → 4", "Dia → 5", "Dia → 6", "Dia → 7", "Dia → 8")
            for elemento in francos_Coria:
                print(elemento)
            print(" ")

        elif apellido.lower() == "rosales":
            print("Los francos de Rosales  son:")
            print("MARZO")
            francos_Rosales = ("Dia → 1", "Dia → 2", "Dia → 3", "Dia → 4", "Dia → 5", "Dia → 6", "Dia → 7", "Dia → 8")
            for elemento in francos_Rosales:
                print(elemento)
            print(" ")

        elif apellido.lower() == "porres":
            print("Los francos de Porres  son:")
            print("MARZO")
            francos_Porres = ("Dia → 1", "Dia → 2", "Dia → 3", "Dia → 4", "Dia → 5", "Dia → 6", "Dia → 7", "Dia → 8")
            for elemento in francos_Porres:
                print(elemento)
            print(" ")