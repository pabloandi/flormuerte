from pygame.color import Color
from pygame import freetype


class Aminoacido:
    """Clase Aminoácido para dibujar el color y establecer la letra"""

    def __init__(self, screen, aminoacido, pos):
        """
        Inicializa la posición, Surface y el aminoacido.
        Los colores de los aminoacidos está basada en la
        siguiente imagen:
        https://www.yourgenome.org/sites/default/files/images/illustrations/codon_wheel_yourgenome.png

        :param screen: pygame.screen.Surface
        :param aminoacido: string
        :param pos: tuple
        """
        self.screen = screen
        self.posicion = pos
        self.aminoacido = aminoacido
        
        self.A = Color('GREEN')
        self.T = Color('RED')
        self.G = Color('YELLOW')
        self.C = Color('BLUE')
        self.U = Color('ORANGE')
        self.otro = Color('GREY')
        self.color = None
        self.setColor(aminoacido)
        self.draw()

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

    def draw(self):
        """
        Inicializa la fuente (por defecto del sistema) y
        la pinta en el lienzo con la posición, letra y color establecidas
        :return:
        """
        # print(self.posicion)
        freetype.init()
        font = freetype.Font(None, 12)
        font.render_to(surf=self.screen, dest=self.posicion, text=self.aminoacido, fgcolor=self.color)
