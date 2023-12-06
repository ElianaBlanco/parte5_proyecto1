import os
import random

class Juego:
    def __init__(self, mapa, inicio, final):
        self.mapa = mapa
        self.inicio = inicio
        self.final = final
        self.px, self.py = inicio

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_mapa(self):
        for fila in self.mapa:
            print("".join(fila))

    def mover_jugador(self, movimiento):
        nueva_px, nueva_py = self.px, self.py

        if movimiento == 'w':
            nueva_py -= 1
        elif movimiento == 's':
            nueva_py += 1
        elif movimiento == 'a':
            nueva_px -= 1
        elif movimiento == 'd':
            nueva_px += 1

        if (
            0 <= nueva_px < len(self.mapa[0]) and
            0 <= nueva_py < len(self.mapa) and
            self.mapa[nueva_py][nueva_px] != '#'
        ):
            self.mapa[self.py][self.px] = '.'
            self.px, self.py = nueva_px, nueva_py
            self.mapa[self.py][self.px] = 'P'
            return True
        else:
            return False

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        mapa, inicio, final = self.leer_mapa_aleatorio(path_a_mapas)
        super().__init__(mapa, inicio, final)

    def leer_mapa_aleatorio(self, path_a_mapas):
        archivos = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(archivos)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            datos = archivo.readlines()

            # Extraer las coordenadas de inicio y fin del archivo
            dimensiones = datos[0].split()
            filas, columnas = int(dimensiones[0]), int(dimensiones[1])
            inicio = tuple(map(int, datos[1].split()))
            final = tuple(map(int, datos[2].split()))

            # Extraer el mapa del archivo
            mapa = [linea.strip() for linea in datos[3:]]

        return mapa, inicio, final
