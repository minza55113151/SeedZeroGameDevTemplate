import pygame
from Assets.assetLoader import AssetLoader
from gameSetting import CARD_WIDTH, CARD_HEIGHT


class Card:
    """Card class, represent a card in the game
    """

    # card face down
    faceDown = pygame.transform.scale(AssetLoader.cardFaceDown, (CARD_WIDTH, CARD_HEIGHT))

    def __init__(self, suit: str, rank: str,  width: float = CARD_WIDTH, height: float = CARD_HEIGHT, spritePath: str = None):
        """Create a card with specific suit and rank

        Args:
            suit (str): suit of the card (spade, heart, club, diamond)
            rank (str): rank of the card (1, 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K) T is ten
            width (float, optional): width of the card. Defaults to cardWidth.
            height (float, optional): height of the card. Defaults to cardHeight.
            spritePath (str, optional): sprite path of the card. Defaults to None.
        """
        self.suit = suit
        self.rank = rank
        self.value = self.__calculateValue(rank=rank)

        self.image = pygame.image.load(
            f"Assets/Images/CuteCardSprite/{self.suit}-{self.rank}.png") \
            if spritePath is None else pygame.image.load(spritePath)
        self.__scaleImage(width=width, height=height)

    def render(self, screen: pygame.Surface, posX: float, posY: float, faceDown: bool = False):
        """Draw the card on the screen

        Args:
            screen (pygame.Surface): screen to draw the card
            posX (float): left position of the card
            posY (float): top position of the card
            faceDown (bool, optional): whether the card is face down. Defaults to False.
        """
        if faceDown:
            screen.blit(self.faceDown, (posX, posY), self.rect)
        elif not faceDown:
            screen.blit(self.image, (posX, posY), self.rect)

    def __scaleImage(self, width: float, height: float):
        """Scale the image of the card

        Args:
            width (float): the width of the card
            height (float): the height of the card
        """
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

    def __calculateValue(self, rank: str) -> int:
        """Calculate the value of the card

        Args:
            rank (str): number or letter of the card

        Returns:
            int: Value of the card
        """
        rankToValueMap = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "T": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
        }

        return rankToValueMap[rank]
