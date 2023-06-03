class Servicio:
    def __init__(self):
        self.servicios = []

    def traer_servicios(self):
        matriz = []
        with open("Resources/servicios.txt", "r") as file:
            for line in file:
                line = line.rstrip().split(sep=";")
                matriz.append(line)
        return matriz

    def cargar_servicios(self, servicios):
        self.servicios = servicios




