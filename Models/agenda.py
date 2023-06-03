import datetime

from self import self


class Agenda:
    def __init__(self):
        self.registros_agenda = []
    def set_reserva(self):
        fecha = input("INGRESE LA FECHA(dd/mm/aaaa) QUE DESEA RESERVAR: ")
        titular = input("INGRESE EL NOMBRE Y APELLIDO DE QUIEN RESERVA: ")
        monto_total = input("INGRESE EL MONTO TOTAL DE LOS SERVICIOS CONTRATADOS: ")
        monto_seña = input("INGRESE EL MONTO QUE SE ABONA DE SEÑA: ")
        with open("../Resources/agenda.txt", "a") as file:
            file.write(f"{fecha};{titular};{monto_total};{monto_seña}\n")
        print("¡¡ Su reserva se guardo CORRECTAMENTE !!")
        print(f"{fecha};{titular};{monto_total};{monto_seña}\n")

    def get_reserva(self, fecha):
        for line in self.registros_agenda:
            if line[0] == fecha:
                disponibilidad = True
                break
            else:
                disponibilidad = False
        return disponibilidad

    def mod_reserva(self, busqueda, pos_modificado, modificador):
        matriz = []

        with open("../Resources/agenda.txt", "r+") as file:
            for line in file.readlines():
                campos = []
                campos = line.split(sep=";")
                matriz.append(campos)
        for aux in range(len(matriz)):
            line = []
            line = matriz[aux]
            if line[0] == busqueda:
                line[int(pos_modificado)] = modificador
                matriz[aux] = line
                break
            else:
                pass
        print(matriz)
        with open("../Resources/agenda.txt", "w") as file:
            for line in matriz:
                actualizacion = ""
                for argument in line:
                    actualizacion += argument + ";"
                # actualizacion += "\n"
                actualizacion = actualizacion.rstrip(";")
                file.write(actualizacion)

    def traer_registros(self):
        matriz = []
        with open("./Resources/agenda.txt", "r") as file:
            for line in file:
                line = line.rstrip().split(sep=";")
                matriz.append(line)
        return matriz

    def cargar_registros(self, registros):
        self.registros_agenda = registros

    def consultar_reserva(self, fecha):
        registro = []
        for line in self.registros_agenda:
            if line[0] == str(fecha):
                registro = line
                break
        return registro



mi_agenda = Agenda
# mi_agenda.set_reserva(self, "12/34/5678", "Matias", 123578, 986)
# mi_agenda.set_reserva(self, datetime.datetime.now(), "Nicolas", 23456, 5567)
# mi_agenda.get_reserva(self, "12/34/5678")
# mi_agenda.mod_reserva(self, "12/34/5678", 1, "Juan")
# mi_agenda.get_reserva(self, "12/34/5678")
