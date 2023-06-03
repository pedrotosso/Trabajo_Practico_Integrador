from self import self
from Models.servicio import Servicio
from Models.agenda import Agenda
from Views.views_menu import ViewMenu


class Controller:
    op_menu1 = ViewMenu.menu_principal(self)
    if op_menu1 == 1:
