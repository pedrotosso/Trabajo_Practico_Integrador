import datetime

from self import self


class Agenda:
    def set_reserva(self, fecha, titular, monto_total, monto_seña):
        with open("ReservasConfirmadas.txt", "a") as file:
            file.write(f"{fecha};{titular};{monto_total};{monto_seña}\n")

    def get_reserva(self, fecha):
        with open(r"C:\Users\Usuario\PycharmProjects\Trabajo_Practico_Integrador\Modelado\ReservasConfirmadas.txt", "r") as file:
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

        with open("ReservasConfirmadas.txt", "r+") as file:
            for line in file.readlines():
                campos = []
                campos = line.split(sep=";")
                matriz.append(campos)
        for aux in range(len(matriz)):
            line = []
            line = matriz[aux]
            if line[0] == busqueda:
                line[1] = modificador
                matriz[aux] = line
                break
            else:
                pass
        print(matriz)
        with open("ReservasConfirmadas.txt", "w") as file:
            for line in matriz:
                actualizacion = ""
                for argument in line:
                    actualizacion += argument + ";"
                # actualizacion += "\n"
                actualizacion = actualizacion.rstrip(";")
                file.write(actualizacion)




mi_agenda = Agenda
#mi_agenda.set_reserva(self, "12/34/5678", "Matias", 123578, 986)
#mi_agenda.set_reserva(self, datetime.datetime.now(), "Nicolas", 23456, 5567)
mi_agenda.get_reserva(self, "12/34/5678")
mi_agenda.mod_reserva(self, "12/34/5678", 1, "Juan")
mi_agenda.get_reserva(self, "12/34/5678")
