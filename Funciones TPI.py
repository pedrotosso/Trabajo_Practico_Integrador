def pasar_archivo_matriz(nombre_archivo):
    matriz = []

    with open('registros.txt', 'r') as file:
        for line in file.readlines():
            campos = []
            campos = line.split(sep=";")
            matriz.append(campos)
    return matriz


def matriz_a_archivo(matriz):
    with open('registros.txt', 'w') as file:
        for line in matriz:
            actualizacion = ""
            for argument in line:
                actualizacion += argument + ";"
            actualizacion += "\n"
            file.write(actualizacion)


# Esto es para probar las funciones unicamente, se considera que el archivo "registros.txt" seria como la agenda o lo
# que se quiera pasar, eso despúes va a ser una variable que se arma con otra función para llamar "nombre_archivo" y
# así podemos traer todas las matrices que queramos.
matriz = pasar_archivo_matriz("hola")
print(matriz)
linea_prueba = ["18/09/2023", "Nicolas Otamendi", "24280570"]
matriz.append(linea_prueba)
matriz_a_archivo(matriz)
