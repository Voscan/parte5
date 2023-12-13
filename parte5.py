import os
import random

class Juego:
    def __init__(self, mapa):
        self.mapa = mapa

    def iniciar_juego(self):
        print(f"Iniciando juego con el mapa:\n{self.mapa}")

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        mapa_elegido = self.seleccionar_mapa_aleatorio(path_a_mapas)
        super().__init__(mapa_elegido)

    def seleccionar_mapa_aleatorio(self, path_a_mapas):
        archivos_mapas = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(archivos_mapas)
        path_completo = f"{path_a_mapas}/{nombre_archivo}"
        return self.leer_mapa(path_completo)

    def leer_mapa(self, path_completo):
        with open(path_completo, 'r') as archivo:
            contenido = archivo.readlines()

        # Obtener las coordenadas de inicio y fin
        coords = contenido[0].split()
        inicio = (int(coords[0]), int(coords[1]))
        fin = (int(coords[2]), int(coords[3]))

        # Unir el resto de las líneas para obtener el mapa
        mapa = ''.join(contenido[1:]).strip()

        return {'inicio': inicio, 'fin': fin, 'mapa': mapa}

# Ruta a tu carpeta de mapas
path_a_mapas = "/Users/user/Desktop/Ada School/Laberinto/parte5/"

# Uso de las clases
juego_archivo = JuegoArchivo(path_a_mapas)
juego_archivo.iniciar_juego()

