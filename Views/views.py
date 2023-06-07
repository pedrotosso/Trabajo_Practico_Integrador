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

    #Reserva

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

    def modificar_reserva(self):
        opcion = ("INGRESE QUE DATO DE LA RESERVA DESEA MODIFICAR 1: FECHA 2: NOMBRE 3 SERVICIOS CONTRATADOS 4: SALIR")

        return opcion
    
    def baja_reserva(self):
        fecha = input("INGRESE LA FECHA DE LA RESERVA QUE QUIERE CANCELAR: ")
#usuario
    def pedir_datos_titular(self):
        nombre = input("INGRESE EL NOMBRE DEL TITULAR DE LA RESERVA: ")
        dni = input("INGRESE EL DNI DEL TITULAR DE LA RESERVA: ")

        return nombre, dni
    
    def modificar_datos_titular(self):
        print("Ingrese que dato quiere modificar 1: Nombre 2: DNI 3: Salir")
        nombre_nuevo = input("INGRESE EL NUEVO NOMBRE DEL TITULAR DE LA RESERVA: ")
        dni_nuevo = ("INGRESE EL NUEVO DNI DEL TITULAR DE LA RESERVA: ")

        return nombre_nuevo, dni_nuevo
    
    def dar_baja_usuario(self):
        dni_baja = input("INGRESE SU DNI PARA DARSE DE BAJA DEL SISTEMA : ")

        return dni_baja
    
    def consultar_datos(self):
        print("SUS DATOS SON :")
        print("Nombre: DNI: ")


#SERVICIOS

    def reservar_servicio(self):
        opcion = input("Ingrese que servicio desea contratar:?\n 1;DJ \n 2;Decoracion \n 3;Cotillon \n 4;Maquina de humo \n 5;Maquillaje \n 6;Musica en vivo \n 7;Locutor \n 8;Fotografo \n 9;Catering \n 10;Barra movil")

        return opcion

    def cancelar_servicio(self):
        print("servicios contratados por el loco y elije los que quiere sacar")
    