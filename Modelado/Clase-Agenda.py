import datetime

from self import self


class Agenda:
    def __init__(self, fecha, estado="True"):
        self.fecha = fecha
        self.estado = estado

    def set_reserva(self, fecha, titular, monto_total, monto_seña):
        line = f"{fecha};{titular};{monto_total};{monto_seña}\n"
        with open("ReservasConfirmadas.txt", "a") as file:
            file.write(line)

    def get_reserva(self, fecha):
        matriz = []
        with open("ReservasConfirmadas.txt", "r") as file:
            for line in file:
                line = line.rstrip()
                separador = ";"
                linea = line.split(separador)
                # print(linea)
                matriz.append(linea)
            for reserva in matriz:
                if reserva[0] == fecha:
                    print(f"La fecha: {reserva[0]} esta reservada por el señor: {reserva[1]}")
        # for lista in matriz:
        #     print(" ", lista, end="\n")
        # print(" ")

    def mod_reserva(self, busqueda, pos_modificado, modificador):
        matriz = []
        reserv_not_mod = []
        reserv_mod = []
        with open("ReservasConfirmadas.txt", "w+") as file:
            for line in file:
                line = line.rstrip()
                separador = ";"
                line = line.split(separador)
                if line[0] == busqueda or line[1] == busqueda or line[2] == busqueda or line[3] == busqueda:
                    reserv_not_mod = line
                    print(reserv_not_mod)
                    line[int(pos_modificado)] = modificador
                    reserv_mod = line
                    print(reserv_mod)
                matriz.append(line)
            for lista in matriz:
                file.write(lista)




mi_agenda = Agenda
mi_agenda.set_reserva(self, "123456", "Matias", 123578, 986)
mi_agenda.set_reserva(self, datetime.datetime.now(), "Nicolas", 23456, 5567)
mi_agenda.get_reserva(self, "123456")
print(mi_agenda.mod_reserva(self, "123456", "2", "Juan"))
