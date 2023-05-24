from self import self

from Modelado.agenda import Agenda
from Modelado.servicio import Servicio

mi_agenda = Agenda()
op_menu = input("¡¡ BIENVENIDOS !!\nMENU:\n1.-CONSULTAR ESTADO DE UNA FECHA\n2.-GENERAR UNA RESERVA\n3.-CONSULTAR UNA "
                "RESERVA REGISTRADA\nINGRESE LA OPCIÓN ELEGIDA: ")
if op_menu == "1":
    mi_agenda.get_reserva()
if op_menu == "2":
    mi_agenda.set_reserva(fecha=input("Ingrese la fecha que desea cargar en el formato dd/mm/mmmm: "), titular=input("Ingrese el nombre del titular de la reserva: "), monto_total=input("Ingrese el monto total de los servicios solicitados: "), monto_seña=input("Ingrese el monto de seña que se abono para la reserva: "))
if op_menu == "3":
    mi_agenda.get_reserva(fecha=input("Ingrese la fecha que desea consultar en el formato dd/mm/mmmm: "))