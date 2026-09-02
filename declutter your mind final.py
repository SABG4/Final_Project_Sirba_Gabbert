import pygame, sys, os
from button import Button

# pygame setup
pygame.init()

X = 940
Y = 640
SCREEN = pygame.display.set_mode((X, Y))

# filling the screen with a color
SCREEN.fill('lightsalmon3')

# set the pygame window name
pygame.display.set_caption('✨declutter your mind✨')

#including sound into my game
pygame.mixer.music.load('media/music.mp3')
pygame.mixer.music.play(-1)

# create a surface object, image is drawn on it.
imp = pygame.image.load("media/start screen.jpg").convert_alpha()
imp = pygame.transform.smoothscale(imp, (860, 560))


def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.SysFont("Monoid", size)

def play():
        pygame.display.set_caption('your messy room😱')
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("lightsalmon3")

            PLAY_ROOM = pygame.image.load("media/room.jpg").convert_alpha()
            PLAY_ROOM = pygame.transform.smoothscale(PLAY_ROOM, (860, 560))
            SCREEN.blit(PLAY_ROOM, (40, 40))

            PLAY_BACK = Button(image=None, pos=(77, 22),
                           text_input="BACK", font=get_font(65), base_color="White", hovering_color="#82cf88")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        start_screen()

            pygame.display.update()


def info():
    pygame.display.set_caption('what is happening')
    while True:
        INFO_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("lightsalmon3")

        INFO_SCREEN = pygame.image.load("media/infopage.jpg").convert_alpha()
        INFO_SCREEN = pygame.transform.smoothscale(INFO_SCREEN, (860, 560))
        SCREEN.blit(INFO_SCREEN, (40, 40))

        INFO_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="#82cf88")

        INFO_BACK.changeColor(INFO_MOUSE_POS)
        INFO_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BACK.checkForInput(INFO_MOUSE_POS):
                    return()

        pygame.display.update()

'''def set_the_mood():
    pygame.display.set_caption('what is happening')
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("lightsalmon3")

        INFO_SCREEN = pygame.image.load("media/room.jpg").convert_alpha()
        INFO_SCREEN = pygame.transform.smoothscale(INFO_SCREEN, (860, 560))
        screen.blit(INFO_SCREEN, (40, 40))

        INFO_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="#82cf88")

        INFO_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    start_screen()

        pygame.display.update()
'''

# main menu/ start screen used from github: baraltech and adapted for my specific cases
def start_screen():
    pygame.display.set_caption('✨start screen✨')

    SCREEN.fill('lightsalmon3')
    while True:
        SCREEN.blit(imp, (40, 40))

        MENU_MOUSE_POS = pygame.mouse.get_pos()


        PLAY_BUTTON = Button(image=pygame.transform.smoothscale(pygame.image.load("media/play button.png"),(75,86)), pos=(700, 500),
                             text_input="PLAY", font=get_font(25), base_color="lightsalmon3", hovering_color="#82cf88")

        INFO_BUTTON = Button(image=pygame.transform.smoothscale(pygame.image.load("media/info button.png"), (40, 86)),
                             pos=(580, 500),
                             text_input="INFO", font=get_font(25), base_color="lightsalmon3", hovering_color="#82cf88")

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for button in [INFO_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if INFO_BUTTON.checkForInput(MENU_MOUSE_POS):
                        info()


        pygame.display.update()

start_screen()


'''
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
'''