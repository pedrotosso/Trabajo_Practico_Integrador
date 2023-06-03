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

    def get_reserva(self):
        fecha = input("INGRESE LA FECHA(dd/mm/aaaa) QUE DESEA RESERVAR: ")
        with open("../Resources/agenda.txt", "r") as file:
            for line in file:
                line = line.rstrip()
                reserva = line.split(sep=";")
                if reserva[0] == fecha:
                    print(f"La fecha: {reserva[0]} esta reservada por el señor: {reserva[1]}")
                    break
                else:
                    print(f"La fecha {fecha} esta disponible")

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

    def




mi_agenda = Agenda
# mi_agenda.set_reserva(self, "12/34/5678", "Matias", 123578, 986)
# mi_agenda.set_reserva(self, datetime.datetime.now(), "Nicolas", 23456, 5567)
# mi_agenda.get_reserva(self, "12/34/5678")
# mi_agenda.mod_reserva(self, "12/34/5678", 1, "Juan")
# mi_agenda.get_reserva(self, "12/34/5678")
