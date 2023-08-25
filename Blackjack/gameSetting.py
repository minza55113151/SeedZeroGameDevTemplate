SUIT_LIST = ["spade", "heart", "club", "diamond"]
RANK_LIST = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

# game size (card, window, button, etc.)
SCALE = 1.5
SCREEN_SIZE = (int(800 * SCALE), int(600 * SCALE))

CARD_WIDTH = 60 * SCALE
CARD_HEIGHT = 90 * SCALE

SOUND_VOLUME = 0.5

BACKGROUND_COLOR = "#21553b"

FPS = 60

# region read
ALL_PHASE = ["playerTurn", "dealerTurn",
            "playerWin", "playerLose", "playerDraw"]

"""Card Class for representing a card
methods:
    __init__: create a card with specific suit and rank
    render: render the card on the screen
"""

"""Deck class for representing a deck of card
methods:
    __init__: create a deck of card with all combination of suit and rank 
            and shuffle it
    drawCard: draw the card from the deck and return it
    render: render the deck of card on the screen
"""

"""Hand class for representing a hand of card (each player's hand)
methods:
    __init__: create a hand of card
    addCard: add a card to the hand
    render: render the hand of card on the screen
"""

"""Button class for representing a button
methods:
    __init__: create a button with specific text, position, width, height, color, text color
    isMouseHover: check if the mouse is hover on the button
    render: render the button on the screen
"""
# endregion
