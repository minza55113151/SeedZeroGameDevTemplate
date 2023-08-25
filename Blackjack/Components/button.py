import pygame
import threading
from Assets.assetLoader import AssetLoader


class Button:
    """Button class for the game
    """
    imageButton = AssetLoader.imageButton
    imageButtonPress = AssetLoader.imageButtonPress

    def __init__(self, text: str, posX: float, posY: float, width: float = 100, height: float = 50,
                 fontSize: int = 20, interactTime: float = 0.2):
        self.text = text
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.fontSize = fontSize
        self.interactTime = interactTime
        self.image = pygame.transform.scale(
            self.imageButton, (int(self.width), int(self.height)))
        self.font = pygame.font.SysFont("Arial", self.fontSize, True)
        self.rect = pygame.Rect(self.posX, self.posY, self.width, self.height)
        self.thread = None

    def setPosition(self, posX: float, posY: float):
        """Set button position

        Args:
            posX (float): X axis position
            posY (float): Y axis position
        """
        self.posX = posX
        self.posY = posY
        self.rect = pygame.Rect(self.posX, self.posY, self.width, self.height)

    def render(self, screen: pygame.Surface):
        """Draw the button on the screen

        Args:
            screen (pygame.Surface): screen to draw the button on
        """
        screen.blit(self.image, (self.posX, self.posY))

        text = self.font.render(self.text, True, "#000000")
        textRect = text.get_rect()
        textRect.center = (self.posX+self.width/2, self.posY+self.height/2)
        screen.blit(text, textRect)

    def isMouseHover(self) -> bool:
        """Check if mouse hovering on the button

        Returns:
            bool: True if mouse hovering on the button, False otherwise
        """
        mousePos = pygame.mouse.get_pos()

        if not self.rect.collidepoint(mousePos):
            return False
        if self.thread is not None and self.thread.is_alive():
            return False

        self.image = pygame.transform.scale(
            self.imageButtonPress, (int(self.width), int(self.height)))
        self.thread = threading.Timer(self.interactTime, self.__resetSprite)
        self.thread.start()

        return True

    def __resetSprite(self):
        """Reset button sprite to normal
        """
        self.image = pygame.transform.scale(
            self.imageButton, (int(self.width), int(self.height)))
