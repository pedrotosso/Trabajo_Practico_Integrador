import self

from Controller.controller import Controller

controlador = Controller()
controlador.inicializador()
controlador.mostrar_msj_bienvenida()
entrada_menu = controlador.menu_principal()
if entrada_menu == 1:
    controlador.consultar_fecha()
if entrada_menu == 2:
    controlador.reg_reserva()
if entrada_menu == 3:
    controlador.consultar_reserva()



