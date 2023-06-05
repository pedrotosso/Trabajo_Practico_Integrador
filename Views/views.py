class View:

    def msj_bienvenida(self):
        print("¡¡ BIENVENIDOS A SOCIAL EVENT SA !!")

    def menu_principal(self):
        try:
            eleccion = int(input("1.-Consultar disponibilidad de fecha\n2.-Registrar Reserva\n3.-Consultar "
                                 "Reserva\n5.-Modificar Reserva\n6.-Cancelar Reserva\n7.-Salir\nPOR FAVOR INGRESE EL "
                                 "NÚMERO DE LA OPCION ELEGIDA: "))
            while 1 > eleccion > 6:
                eleccion = input("1.-Consultar disponibilidad de fecha\n2.-Registrar Reserva\n3.-Consultar "
                                 "Reserva\n5.-Modificar Reserva\n6.-Cancelar Reserva\n7.-Salir\nPOR FAVOR INGRESE EL "
                                 "NÚMERO DE LA OPCION ELEGIDA: ")
        except ValueError:
            while 1 > eleccion > 6 or isinstance(eleccion, str):
                eleccion = int(input("1.-Consultar disponibilidad de fecha\n2.-Registrar Reserva\n3.-Consultar "
                                     "Reserva\n5.-Modificar Reserva\n6.-Cancelar Reserva\n7.-Salir\nPOR FAVOR INGRESE "
                                     "EL NÚMERO DE LA OPCION ELEGIDA: "))
        return eleccion

    def pedir_fecha(self):
        fecha = input("INGRESE LA FECHA QUE DESEA CONSULTAR: ")
        return fecha

    def respuesta_disponibilidad(self, disponibilidad, fecha=None):
        if disponibilidad:
            print("¡¡ LA FECHA ESTA DISPONIBLE !!")
        else:
            print(f"¡¡ LA FECHA ESTA RESERVADA !!\nLA FECHA MAS PROXIMA DISPONIBLE ES: {fecha}")


    def mostrar_reserva(self, registro):
        print(f"FECHA RESERVADA: {registro[0]}\nTITULAR DE LA RESERVA: {registro[1]}\nFECHA DE INGRESO DE LA RESERVA: {registro[2]}\nMONTO TOTAL DE LA RESERVA: {registro[3]}\nMONTO ABONADO DE SEÑA: {registro[4]}")

    def pedir_nombre_dni(self):
        nombre = input("INGRESE EL NOMBRE DEL TITULAR DE LA RESERVA: ")
        dni = input("INGRESE EL DNI DEL TITULAR DE LA RESERVA: ")

        return nombre, dni

