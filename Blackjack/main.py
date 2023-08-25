import pygame
import threading
from Components.button import Button
from Components.deck import Deck
from Components.hand import Hand
from Assets.assetLoader import AssetLoader
from gameSetting import SCREEN_SIZE, BACKGROUND_COLOR, FPS

pygame.init()

loseImage = AssetLoader.loseImage
winImage = AssetLoader.winImage
drawImage = AssetLoader.drawImage

loseSound = AssetLoader.loseSound
winSound = AssetLoader.winSound
drawSound = AssetLoader.drawSound

screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
clock = pygame.time.Clock()


def main():
    global isGameRunning, phase, isResettingGame

    while True:
        hitButton = Button(text="Hit", posX=screen.get_width()-150,
                           posY=screen.get_height()//2-40)
        standButton = Button(text="Stand", posX=screen.get_width()-150,
                             posY=screen.get_height()//2+40, interactTime=1000)
        buttonList = [hitButton, standButton]

        # TODO: set data before game start (create deck, hand of player and dealer, and give 2 card to player and dealer)

        isGameRunning = True
        phase = "playerTurn"
        isResettingGame = False

        while isGameRunning:
            clock.tick(FPS)
            pygame.display.set_caption(f"BlackJack - {phase}")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    # TODO: may need to add more parameter to the below function
                    ManageButtonEvent(buttonList=buttonList)
                if event.type == pygame.VIDEORESIZE:
                    hitButton.setPosition(
                        posX=screen.get_width()-150, posY=screen.get_height()//2-40)
                    standButton.setPosition(
                        posX=screen.get_width()-150, posY=screen.get_height()//2+40)

            # TODO: check game phase by calling _ function
            gamePhaseHandler()

            # TODO: draw all object on screen (may need to add more object to draw function)
            render(screen=screen, buttonList=buttonList, phase=phase)
            pygame.display.update()


def ManageButtonEvent(buttonList: list[Button]):
    """This function will manage hitButton and standButton

    Args:
        buttonList (list): list of button
        sometype (type): may need to add the parameter by yourself
        sometype (type): may need to add the parameter by yourself
        sometype (type): may need to add the parameter by yourself
    """
    global phase
    if phase != "playerTurn":
        return

    hitButton, standButton = buttonList
    if hitButton.isMouseHover():
        # TODO: make player draw 1 card
        pass
    elif standButton.isMouseHover():
        # TODO: make dealer draw a card until dealer score >= 17 and change something?
        pass

def playerHit():
    """this function will add a card to player a hand

    Args:
        sometype (type): may need to add the parameter by yourself
        sometype (type): may need to add the parameter by yourself
    """
    # TODO: implement this function
    pass


def dealerHit():
    """this function will add a card to dealer hand untill dealer score >= 17

    Args:
        sometype (type): may need to add the parameter by yourself
        sometype (type): may need to add the parameter by yourself
    """
    # TODO: implement this function
    pass


def render(screen: pygame.Surface, buttonList: list[Button], phase: str):
    """this function will draw all object on screen

    Args:
        screen (pygame.Surface): screen to draw
        buttonList (list): list of button
        phase (str): phase of game
        sometype (type): may need to add the parameter by yourself
        sometype (type): may need to add the parameter by yourself
        sometype (type): may need to add the parameter by yourself
    """
    screen.fill(color=BACKGROUND_COLOR)  # green
    for button in buttonList:
        button.render(screen=screen)

    # TODO: draw something that you want to draw here

    if phase == "playerWin":
        centerPositon = (screen.get_width()/2 - winImage.get_width()/2,
                         screen.get_height()/2 - winImage.get_height()/2)
        screen.blit(winImage, centerPositon)
    elif phase == "playerLose":
        centerPositon = (screen.get_width()/2 - loseImage.get_width()/2,
                         screen.get_height()/2 - loseImage.get_height()/2)
        screen.blit(loseImage, centerPositon)
    elif phase == "playerDraw":
        centerPositon = (screen.get_width()/2 - loseImage.get_width()/2,
                         screen.get_height()/2 - loseImage.get_height()/2)
        screen.blit(drawImage, centerPositon)


def gamePhaseHandler(playerHand: Hand, dealerHand: Hand):
    """this function will handle the game phase

    Args:
        playerHand (Hand): hand of player
        dealerHand (Hand): hand of dealer
    """
    global phase

    isPlayerBust = playerHand.score > 21
    isDealerBust = dealerHand.score > 21
    isDealerCanHit = dealerHand.score < 17
    if phase == "playerTurn":
        if isPlayerBust:
            # TODO: change phase to some phase
            pass

    elif phase == "dealerTurn" and not isDealerCanHit:
        if isDealerBust:
            # TODO: change phase to some phase
            pass
        elif dealerHand.score < playerHand.score:
            # TODO: change phase to some phase
            pass
        elif dealerHand.score > playerHand.score:
            # TODO: change phase to some phase
            pass
        elif dealerHand.score == playerHand.score:
            # TODO: change phase to some phase
            pass

    # when state is playerWin, playerLose, or playerDraw,
    # the game will wait for 1.5 second before start a new game
    global isResettingGame
    if phase in ["playerWin", "playerLose", "playerDraw"] and not isResettingGame:
        isResettingGame = True
        thread = threading.Timer(1.5, setIsGameRunning, [False])
        thread.start()


def setIsGameRunning(value: bool):
    global isGameRunning
    isGameRunning = value


main()
