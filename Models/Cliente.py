import datetime


class Cliente:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def get_nombre(self):
        return self._nombre
    
    def get_dni(self):
        return self._dni
    
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_dni(self, dni):
        self._dni = dni