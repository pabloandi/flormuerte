from Bio import SeqIO
from math import sin,cos
from random import random

from aminoacido import Aminoacido

class Secuencia:
    """
    Cada secuencia esta asociada a una secuencia de ADN.
    El archivo de la secuencia de ADN está en formato Genbank.
    La mayoría de los archivos provienen de NCBI Genome Project
    https://www.ncbi.nlm.nih.gov/genome/

    """
    def __init__(self, screen, archivo ):
        self.archivo = archivo
        self.secuencia = []
        self.camino = []
        self.screen = screen
        self.limites = screen.get_size()
        self.limite_aminoacidos = 800
        self.leer_archivo()
        self.crear_camino()
        

    def leer_archivo(self):
        """
        Lee el archivo de la secuencia con la que fue
        asociado esta secuencia
        :return:
        """
        try:
            self.secuencia = SeqIO.read(self.archivo,'genbank').seq
        except Exception as e:
            pass

    def crear_camino(self):
        """
        Crea el camino de la secuencia.
        Inicia a partir del tope del tronco de la flor
        :return:
        """
        limx,limy = self.limites
        partx = limx // 2
        party = limy // 2
        x=y=0

        r=0
        theta=0

        for aminoacido in self.secuencia[:self.limite_aminoacidos]:
            if (x + partx) < limx and (y + party) < limy:
                x = r * cos(theta)
                y = r * sin(theta)

                am=Aminoacido(self.screen, aminoacido, (x + partx, y + party))

                r += random()
                theta += random()

                del am
            else:
                break


            

