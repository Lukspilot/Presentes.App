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
            francos_Alex = ("Miercoles → 1", "Sabado → 4", "Jueves → 9", "Martes → 14", "Sabado → 18", "Domingo → 19", "Lunes → 27", "Martes → 28")
            for elemento in francos_Alex:
                print(elemento)

        if opcion == 4:
            system("cls")
            print("Los francos de Garcia Lucas son:")
            francos_LucasG = ("Viernes → 3", "Martes → 7", "Sabado → 1", "Domingo → 12", "Jueves → 16", "Miercoles → 22", "Sabado → 25", "Martes → 28")
            for elemento in francos_LucasG:
                print(elemento)

        if opcion == 5:
            system("cls")
            print("Los francos de Aguirre Emiliano son:")
            francos_Emiliano = ("Jueves → 2", "Lunes → 6", "Sabado → 11", "Domingo → 12", "Lunes → 13", "Miercoles → 15", "Martes → 28", "Miercoles → 29")
            for elemento in francos_Emiliano:
                print(elemento)

        if opcion == 6:
            system("cls")
            print("Los francos de Hernandez Lucas son:")
            francos_LucasH = ("Viernes → 3", "Miercoles → 8", "Miercoles → 15", "Sabado → 18", "Domingo → 19", "Jueves → 23", "Domingo → 26", "Martes → 28")
            for elemento in francos_LucasH:
                print(elemento)

        if opcion == 7:
            system("cls")
            print("Los francos de Coria Carlos son:")
            francos_Carlos = ("Sabado → 4", "Domingo → 5", "Miercoles → 8", "Lunes → 13", "Viernes → 17", "Sabado → 18", "Viernes → 24", "Lunes → 27")
            for elemento in francos_Carlos:
                print(elemento)

        if opcion == 8:
            system("cls")
            print("Los francos de Rosales Leandro son:")
            francos_Leandro = ("Viernes → 3", "Viernes → 10", "Lunes → 13", "Viernes → 17", "Domingo → 19", "Jueves → 23", "Sabado → 25", "Domingo → 26")
            for elemento in francos_Leandro:
                print(elemento)

        if opcion == 9:
            system("cls")
            print("Los francos de Porres Lucas son:")
            francos_LucasP = ("Domingo → 5," "Sabado → 11", "Domingo → 12", "Domingo → 19", "Lunes → 20", "Martes → 21", "Sabado → 25", "Domingo → 26")
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
            francos_Alex = ("Lunes → 1", "Martes → 2", "Miercoles → 3", "Jueves → 4", "Viernes → 5", "Sabado → 6", "Domingo → 7", "Lunes → 8")
            for elemento in francos_Alex:
                print(elemento)
            print(" ")

        elif apellido.lower() == "garcia":
            print("Los francos de Garcia son:")
            francos_Lucas_G = ("Lunes → 1", "Martes → 2", "Miercoles → 3", "Jueves → 4", "Viernes → 5", "Sabado → 6", "Domingo → 7", "Lunes → 8")
            for elemento in francos_Lucas_G:
                print(elemento)
            print(" ")

        elif apellido.lower() == "aguirre":
            print("Los francos de Aguirre  son:")
            francos_Aguirre = ("Lunes → 1", "Martes → 2", "Miercoles → 3", "Jueves → 4", "Viernes → 5", "Sabado → 6", "Domingo → 7", "Lunes → 8")
            for elemento in francos_Aguirre:
                print(elemento)
            print(" ")

        elif apellido.lower() == "hernandez":
            print("Los francos de Hernandez  son:")
            francos_Hernandez = ("Lunes → 1", "Martes → 2", "Miercoles → 3", "Jueves → 4", "Viernes → 5", "Sabado → 6", "Domingo → 7", "Lunes → 8")
            for elemento in francos_Hernandez:
                print(elemento)
            print(" ")

        elif apellido.lower() == "coria":
            print("Los francos de Coria  son:")
            francos_Coria = ("Lunes → 1", "Martes → 2", "Miercoles → 3", "Jueves → 4", "Viernes → 5", "Sabado → 6", "Domingo → 7", "Lunes → 8")
            for elemento in francos_Coria:
                print(elemento)
            print(" ")

        elif apellido.lower() == "rosales":
            print("Los francos de Rosales  son:")
            francos_Rosales = ("Lunes → 1", "Martes → 2", "Miercoles → 3", "Jueves → 4", "Viernes → 5", "Sabado → 6", "Domingo → 7", "Lunes → 8")
            for elemento in francos_Rosales:
                print(elemento)
            print(" ")

        elif apellido.lower() == "porres":
            print("Los francos de Porres  son:")
            francos_Porres = ("Lunes → 1", "Martes → 2", "Miercoles → 3", "Jueves → 4", "Viernes → 5", "Sabado → 6", "Domingo → 7", "Lunes → 8")
            for elemento in francos_Porres:
                print(elemento)
            print(" ")