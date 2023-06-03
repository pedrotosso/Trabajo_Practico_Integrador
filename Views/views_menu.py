class ViewMenu:

    def msj_bienvenida(self):
        print("¡¡ BIENVENIDOS A SOCIAL EVENT SA !!")

    def menu_principal(self):
        try:
            eleccion = int(input("1.-Consultar disponibilidad de fecha\n2.-Registrar Reserva\n3.-Consultar "
                                 "Reserva\n5.-Modificar Reserva\n6.-Cancelar Reserva\7.-Salir\nPOR FAVOR INGRESE EL "
                                 "NÚMERO DE LA OPCION ELEGIDA: "))
            while 1 > eleccion > 6:
                eleccion = input("1.-Consultar disponibilidad de fecha\n2.-Registrar Reserva\n3.-Consultar "
                                 "Reserva\n5.-Modificar Reserva\n6.-Cancelar Reserva\7.-Salir\nPOR FAVOR INGRESE EL "
                                 "NÚMERO DE LA OPCION ELEGIDA: ")
        except ValueError:
            while 1 > eleccion > 6:
                eleccion = int(input("1.-Consultar disponibilidad de fecha\n2.-Registrar Reserva\n3.-Consultar "
                                     "Reserva\n5.-Modificar Reserva\n6.-Cancelar Reserva\7.-Salir\nPOR FAVOR INGRESE "
                                     "EL NÚMERO DE LA OPCION ELEGIDA: "))

