logo =""" 
    __________________ 
   |.----------------.|
   || CODEGENERATORS ||
   ||   -._ .-.      ||
   ||   -._| | |     ||
   ||   -._| | |     ||
   ||   -._|.-.|     ||
   ||________________||
   /.-.-.-.-.-.-.-.-.-.\ 
  /.-.-.-.-.-.-.-.-.-.-.\ 
 /.-.-.-.-.-.-.-.-.-.-.-.\ 
/______/__________\___o___\ 
\_________________________/ """

def mostrar_menu():
    print("Menu:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

def obtener_opcion():
    while True:
        opcion = input("Ingrese el número de opción que desea ejecutar: ")
        try:
            opcion = int(opcion)
            if opcion >= 1 and opcion <= 4:
                return opcion
            else:
                print("Error: por favor, ingrese un número válido del 1 al 4.")
        except ValueError:
            print("Error: por favor, ingrese un número válido del 1 al 4.")


#Logo Bienvenida
print(logo)
print("----------------------------")
while True:
    print("==========")
    mostrar_menu()
    opcion = obtener_opcion()

    if opcion == 1:
        print("Ha seleccionado la opción 1.")
    elif opcion == 2:
        print("Ha seleccionado la opción 2.")
    elif opcion == 3:
        print("Ha seleccionado la opción 3.")
    elif opcion == 4:
        print("Saliendo del programa...")
        break
