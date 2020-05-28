from pygame.color import Color
from pygame.sprite import Sprite
from pygame.draw import circle as Circle
from pygame import Surface

from base import Base


class Aminoacido(Sprite, Base):
    """Clase Aminoácido para dibujar el color y establecer la letra"""

    def __init__(self, aminoacido):
        """
        Inicializa la posición, Surface y el aminoacido.
        Los colores de los aminoacidos está basada en la
        siguiente imagen:
        https://www.yourgenome.org/sites/default/files/images/illustrations/codon_wheel_yourgenome.png

        :param aminoacido: string
        :param pos: tuple
        """
        #iniciar clases superiores
        Base.__init__(self)
        Sprite.__init__(self)

        self.aminoacido = aminoacido
        self.radio = int(self.config['aminoacidos']['radio'])
        self.color = None
        
        self.A = Color(0,255,0)
        self.T = Color(255,0,0)
        self.G = Color(255,255,0)
        self.C = Color(0,0,255)
        self.U = Color(255,127,0)
        self.otro = Color(84,84,84)

        self.setColor(aminoacido)

        # crear fondo
        self.image = Surface((self.radio * 2, self.radio * 2))
        self.image.set_alpha(50)
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        
        # dibujar circulo
        Circle(self.image, self.color, (self.radio, self.radio), self.radio)

        self.rect = self.image.get_rect()
        

    def setColor(self, aminoacido):
        """
        Establece el color en el lienzo de acuerdo
        a la letra del aminoacido

        :param aminoacido: string
        :return:
        """

        if aminoacido == 'A':
            self.color = self.A
        elif aminoacido == 'T':
            self.color = self.T
        elif aminoacido == 'G':
            self.color = self.G
        elif aminoacido == 'C':
            self.color = self.C
        elif aminoacido == 'U':
            self.color = self.U
        else:
            self.color = self.otro
        
        
        
        
