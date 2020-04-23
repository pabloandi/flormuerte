from pygame.color import Color
from pygame.sprite import Sprite
from pygame.draw import circle as Circle
from pygame import Surface



class Aminoacido(Sprite):
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
        #iniciar clase superior
        super().__init__()

        self.aminoacido = aminoacido
        self.radio = 10
        self.color = None
        
        # self.A = Color(0,255,0,20) #verde
        # self.T = Color(255,0,0,20) #rojo
        # self.G = Color(255,255,0,20) #amarillo
        # self.C = Color(0,0,255,20) #azul
        # self.U = Color(255,127,0,20) #naranja
        # self.otro = Color(84,84,84,20) #gris

        self.A = Color(0,255,255) #cyan
        self.T = Color(255,0,255) #magenta
        self.G = Color(255,255,0) #amarillo
        self.C = Color(0,0,0) #negro
        self.U = Color(255,127,0) #naranja
        self.otro = Color(84,84,84) #gris

        self.setColor(aminoacido)

        # crear fondo
        self.image = Surface((self.radio * 2, self.radio * 2))
        self.image.set_alpha(50)
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))
        
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
        
        
        
        
