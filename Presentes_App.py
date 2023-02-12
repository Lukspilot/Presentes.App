#Arranque
from os import system
system("cls")
import time
print("Hola, bienvenido!")
time.sleep(1)
from os import system
system("cls")

#Menu opciones 
while True:
    print("Menú de opciones:")
    print("1. Ver lista de camilleros")
    print("2. Buscar por apellido")
    
    opcion = int(input("Elija una opción: "))

#Menu opciones 1
    if opcion == 1:
        
        from os import system
        system("cls")
        
        print("3. Silva Alex")
        print("4. Garcia Lucas")
        print("5. Aguirre Emiliano")
        print("6. Hernandez Lucas")
        print("7. Coria Carlos")
        print("8. Rosales Leandro")
        print("9. Porres Lucas")
        print("10. <-Regresar al menú anterior")
        opcion = int(input("Elija una opción: "))
        
        if opcion == 3:
            from os import system
            system("cls")
            
            print("Los francos de Silva Alex son:")
            
            francos_Alex = ("Miercoles 1", "Sabado 4", "Jueves 9", "Martes 14", "Sabado 18", "Domingo 19", "Lunes 27", "Martes 28")
            for elemento in francos_Alex:
                print(elemento)
        
        if opcion == 4:
            from os import system
            system("cls")
            
            print("Los francos de Garcia Lucas son:")
            
            francos_LucasG = ("Viernes 3", "Martes 7", "Sabado 11", "Domingo 12", "Jueves 16", "Miercoles 22", "Sabado 25", "Martes 28")
            for elemento in francos_LucasG:
                print(elemento)
        
        if opcion == 5:
            from os import system
            system("cls")
            
            print("Los francos de Aguirre Emiliano son:")
            
            francos_Emiliano = ("Jueves 2", "Lunes 6", "Sabado 11", "Domingo 12", "Vacaciones desde el Lunes 13 hasta el Domingo 26", "Martes 28")
            for elemento in francos_Emiliano:
                print(elemento)

        if opcion == 6:
            from os import system
            system("cls")
            
            print("Los francos de Hernandez Lucas son:")
            
            francos_LucasH = ("Licencia medica del 1 al 3", "Sabado 4", "Domingo 5", "Vacaciones desde el Lunes 6 hasta el Domingo 12", "Licencia medica desde el Lunes 13 hasta el Viernes 24", "Domingo 26", "Vacaciones Lunes 27 hasta-> Proximo mes")
            for elemento in francos_LucasH:
                print(elemento)

        if opcion == 7:
            from os import system
            system("cls")
            
            print("Los francos de Coria Carlos son:")
            
            francos_Carlos = ("Sabado 4", "Domingo 5", "Miercoles 8", "Lunes 13", "Viernes 17", "Sabado 18", "Viernes 24", "Lunes 27")
            for elemento in francos_Carlos:
                print(elemento)

        if opcion == 8:
            from os import system
            system("cls")
            
            print("Los francos de Rosales Leandro son:")
            
            francos_Leandro = ("Viernes 3", "Viernes 10", "Lunes 13", "Viernes 17", "Domingo 19", "Jueves 23", "Sabado 25", "Domingo 26")
            for elemento in francos_Leandro:
                print(elemento)

        if opcion == 9:
            from os import system
            system("cls")
            
            print("Los francos de Porres Lucas son:")
            
            francos_LucasP = ("Domingo 5" "Vacaciones desde el Lunes 6 hasta el Miercoles 8", "Sabado 11", "Domingo 12", "Domingo 19", "Lunes 20", "Martes 21", "Sabado 25", "Domingo 26")
            for elemento in francos_LucasP:
                print(elemento)

        if opcion == 10:
            from os import system
            system("cls")
            
            continue
    
    elif opcion == 2:
        from os import system
        system("cls")
        
        buscar = str(input("Ingrese apellido del camillero: "))
        
        if buscar == "Silva":
            print("Los francos de Silva Alex son:")
            
            francos_Alex = ("Miercoles 1", "Sabado 4", "Jueves 9", "Martes 14", "Sabado 18", "Domingo 19", "Lunes 27", "Martes 28")
            for elemento in francos_Alex:
                print(elemento)
        
        if buscar == "Garcia":
            print("Los francos de Garcia Lucas son:")
            
            francos_LucasG = ("Viernes 3", "Martes 7", "Sabado 11", "Domingo 12", "Jueves 16", "Miercoles 22", "Sabado 25", "Martes 28")
            for elemento in francos_LucasG:
                print(elemento)
        
        if buscar == "Aguirre":
            print("Los francos de Aguirre Emiliano son:")
            
            francos_Emiliano = ("Jueves 2", "Lunes 6", "Sabado 11", "Domingo 12", "Vacaciones desde el Lunes 13 hasta el Domingo 26", "Martes 28")
            for elemento in francos_Emiliano:
                print(elemento)
                
        if buscar == "Hernandez":
            print("Los francos de Hernandez Lucas son:")
            
            francos_LucasH = ("Licencia medica del 1 al 3", "Sabado 4", "Domingo 5", "Vacaciones desde el Lunes 6 hasta el Domingo 12", "Licencia medica desde el Lunes 13 hasta el Viernes 24", "Domingo 26", "Vacaciones Lunes 27 hasta-> Proximo mes")
            for elemento in francos_LucasH:
                print(elemento)
                
        if buscar == "Coria":
            print("Los francos de Coria Carlos son:")
            
            francos_Carlos = ("Sabado 4", "Domingo 5", "Miercoles 8", "Lunes 13", "Viernes 17", "Sabado 18", "Viernes 24", "Lunes 27")
            for elemento in francos_Carlos:
                print(elemento)
                
        if buscar == "Rosales":
            print("Los francos de Rosales Leandro son:")
            
            francos_Leandro = ("Viernes 3", "Viernes 10", "Lunes 13", "Viernes 17", "Domingo 19", "Jueves 23", "Sabado 25", "Domingo 26")
            for elemento in francos_Leandro:
                print(elemento)
                
        if buscar == "Porres":
            print("Los francos de Porres Lucas son:")
            
            francos_LucasP = ("Domingo 5" "Vacaciones desde el Lunes 6 hasta el Miercoles 8", "Sabado 11", "Domingo 12", "Domingo 19", "Lunes 20", "Martes 21", "Sabado 25", "Domingo 26")
            for elemento in francos_LucasP:
                print(elemento)
        break


print("Fin del programa")