from pathlib import Path
from secuencia import Secuencia

import pygame

class Flor:
    """Lee los archivos de las secuencias de adn y crea ramas con cada uno"""

    def __init__(self):
        """Inicializa la flor leyendo las carpetas de las secuencias de virus y bacterias"""
        self.pathvirus = Path("./material/virus").resolve()
        self.pathbacterias = Path("./material/bacteria").resolve()
        self.archivos_secuencias = [archivo for archivo in self.pathvirus.iterdir()] + [archivo for archivo in self.pathbacterias.iterdir()]
        # limitar el número de secuencias con el proposito de optimizacion de recursos de máquina
        self.limite_secuencias = 100


    def pintar(self, screen):
        """Pintar todos los elementos de la flor"""
        self.screen = screen
        self.pintar_tronco()
        self.pintar_secuencias()

    def pintar_tronco(self):
        """Pintar el tronco de la flor"""
        TRONCO =  pygame.Color('BROWN')
        ancho, alto = self.screen.get_size()
        #
        pygame.draw.rect(self.screen, TRONCO, (
            (ancho // 2) - 10, alto, 20, -( alto // 2 )
        ))

    def pintar_secuencias(self):
        """Pinta las secuencias de la flor. Cada una es una secuencia ADN de virus o bacteria"""
        for sec in self.archivos_secuencias[:self.limite_secuencias]:
            Secuencia(self.screen, sec)
