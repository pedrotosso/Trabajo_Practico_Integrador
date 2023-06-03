from self import self
from Models.servicio import Servicio
from Models.agenda import Agenda
from Views.views import View


class Controller:

    def mostrar_msj_bienvenida(self):
        View.msj_bienvenida(self)

    def menu_principal(self):
        op_menu1 = View.menu_principal(self)
        return op_menu1

    def consultar_fecha(self):
        fecha = View.pedir_fecha(self)
        disponible = Agenda.get_reserva(self, fecha=fecha)
        View.respuesta_disponibilidad(self, disponibilidad=disponible)

    def inicializador(self):
        Servicio.cargar_servicios(self, servicios=Servicio.traer_servicios(self))
        Agenda.cargar_registros(self, registros=Agenda.traer_registros(self))

    def consultar_reserva(self):
        fecha = View.pedir_fecha(self)
        control = Agenda.get_reserva(self, fecha=fecha)
        if control:
            registro = Agenda.consultar_reserva(self, fecha=fecha)
            View.mostrar_reserva(self, registro=registro)
        else:
            View.respuesta_disponibilidad(self, disponibilidad=control)

