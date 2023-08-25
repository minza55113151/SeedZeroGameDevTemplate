import pygame
import random
from gameSetting import SUIT_LIST, RANK_LIST, CARD_WIDTH, CARD_HEIGHT
from Components.card import Card


class Deck:
    """
    Deck class, represent a deck of card
    """

    def __init__(self):
        """
        Create a deck of card with all combination of suit and rank
        """
        self.allCard = [Card(suit=suit, rank=rank)
                        for suit in SUIT_LIST for rank in RANK_LIST]
        self.__shuffle()

    def render(self, screen: pygame.Surface):
        """
        Draw the deck of card on the screen
        """
        posX = (screen.get_width()-CARD_WIDTH)/2
        posY = (screen.get_height()-CARD_HEIGHT)/2
        for i in range(self.__size):
            screen.blit(
                Card.faceDown, (posX+0.15*i, posY+i*0.15), Card.faceDown.get_rect())

    def drawCard(self) -> Card:
        """
        Draw a card from the deck

        Returns:
            Card: The card that is drawn
        """
        if self.__size == 0:
            raise Exception("Deck is empty")

        return self.allCard.pop()

    @property
    def __size(self):
        """
        Get the size of the deck
        """
        return len(self.allCard)

    def __shuffle(self):
        """
        Shuffle the deck
        """
        random.shuffle(self.allCard)

    # region debug
    def showAllCard(self, screen: pygame.Surface):
        for index, card in enumerate(self.allCard):
            card.render(screen, (index % 13) * CARD_WIDTH,
                        (index//13)*CARD_HEIGHT)

    def printAllCard(self):
        for card in self.allCard:
            print(card.suit + "-" + card.rank)
    # endregion
