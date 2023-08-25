import pygame
from gameSetting import SOUND_VOLUME


class AssetLoader:
    loseImage = pygame.image.load("Assets/Images/lose.png")
    winImage = pygame.image.load("Assets/Images/win.png")
    drawImage = pygame.image.load("Assets/Images/draw.png")

    imageButton = pygame.image.load("Assets/Images/button.png")
    imageButtonPress = pygame.image.load("Assets/Images/button_pressed.png")
    
    cardFaceDown = pygame.image.load("Assets/Images/CuteCardSprite/black.png")
    
    pygame.mixer.init()
    
    loseSound = pygame.mixer.Sound("Assets/Sounds/lose.wav")
    winSound = pygame.mixer.Sound("Assets/Sounds/win.wav")
    drawSound = pygame.mixer.Sound("Assets/Sounds/draw.wav")
    
    loseSound.set_volume(SOUND_VOLUME)
    winSound.set_volume(SOUND_VOLUME)
    drawSound.set_volume(SOUND_VOLUME)