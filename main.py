import self

from Controller.controller import Controller

controlador = Controller()
Controller.inicializador(self)
Controller.mostrar_msj_bienvenida(self)
entrada_menu = Controller.menu_principal(self)
if entrada_menu == 1:
    Controller.consultar_fecha(self)
if entrada_menu == 3:
    Controller.consultar_reserva(self)



