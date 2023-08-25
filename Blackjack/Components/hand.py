import pygame
from gameSetting import CARD_WIDTH, CARD_HEIGHT
from Components.deck import Deck


class Hand:
    """
    Hand class, represent a hand of card (player or dealer hand)
    This class is used to store the card in hand and calculate the score
    """

    def __init__(self, deck: Deck):
        """Create a hand
        """
        self.deck = deck
        self.cards = []
        self.score = 0

    def drawCard(self):
        """Add a card to the hand and calculate the score

        Args:
            card (Card): card to be added
        """
        card = self.deck.drawCard()
        self.cards.append(card)
        self.score += card.value

        sound = pygame.mixer.Sound("Assets/Sounds/drawCard.mp3")
        sound.play()

    def render(self, screen: pygame.Surface, isPlayer: bool, phase: str):
        """Draw cards in hand on the screen and draw the score (Text) on the screen

        Args:
            screen (pygame.Surface): screen to draw the cards
            isPlayer (bool): is this hand belong to the player
            phase (str): phase of the game (playerTurn, dealerTurn)
        """
        self.__renderScore(screen=screen, isPlayer=isPlayer,
                           enabled=(phase != "playerTurn"))
        for index, card in enumerate(self.cards):
            posX, posY = self.__getCardPosition(
                screen=screen, index=index, isPlayer=isPlayer, handsize=self.__size)

            card.render(screen=screen, posX=posX, posY=posY,
                        faceDown=(not isPlayer and index == 0 and phase == "playerTurn"))

    def __renderScore(self, screen: pygame.Surface, isPlayer: bool, enabled: bool = True):
        """Draw the score (Text) on the screen

        Args:
            screen (pygame.Surface): screen to draw the score on
            isPlayer (bool): is this hand belong to the player
            enabled (bool, optional): the score is enabled or not. Defaults to True.
        """
        if isPlayer or enabled:
            text = pygame.font.SysFont("Arial", 20, True).render(
                f"Score: {self.score}", True, "#000000")
        elif not isPlayer:
            text = pygame.font.SysFont("Arial", 20, True).render(
                f"Score: ?+{self.score-self.cards[0].value}", True, "#000000")

        textRect = text.get_rect()
        centerX, centerY = self.__getScorePosition(
            screen=screen, isPlayer=isPlayer)
        textRect.center = (centerX, centerY)
        screen.blit(text, textRect)

    def __getCardPosition(self, screen: pygame.Surface, index: int, isPlayer: bool, handsize: int) -> tuple:
        """Get the position of each card on the hand

        Args:
            screen (pygame.Surface): screen to draw the cards
            index (int): index of the card
            isPlayer (bool): is this hand belong to the player
            handsize (int): size of the hand

        Returns:
            tuple: position of the card
        """
        newWidth = CARD_WIDTH*2//3
        middleX = (screen.get_width()-newWidth)//2
        if isPlayer:
            if handsize % 2 == 0:
                posX = middleX - (handsize//2)*newWidth + newWidth//2
            elif handsize % 2 == 1:
                posX = middleX - (handsize//2)*newWidth
            posY = screen.get_height()-CARD_HEIGHT
        elif not isPlayer:
            if handsize % 2 == 0:
                posX = middleX - (handsize//2)*newWidth + newWidth//2
            elif handsize % 2 == 1:
                posX = middleX - (handsize//2)*newWidth
            posY = 0
        return (posX + index*newWidth, posY)

    def __getScorePosition(self, screen: pygame.Surface, isPlayer: bool):
        """Get the position of the score (Text)

        Args:
            screen (pygame.Surface): screen to draw the score
            isPlayer (bool): is this hand belong to the player

        Returns:
            tuple: position of the score
        """
        posX = (screen.get_width())//2
        posY = screen.get_height()-CARD_HEIGHT*5/4 if isPlayer else CARD_HEIGHT*5/4
        return posX, posY

    @property
    def __size(self):
        """
        Number of cards in hand
        """
        return len(self.cards)
