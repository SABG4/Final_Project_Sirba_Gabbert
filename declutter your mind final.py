import pygame, sys, os
from button import Button

# pygame setup
pygame.init()

X = 940
Y = 640
SCREEN = pygame.display.set_mode((X, Y))

#preloading the music
pygame.mixer.music.load('media/music.mp3')

# set the pygame window name
pygame.display.set_caption('✨declutter your mind✨')

# create a surface object, image is drawn on it.
imp = pygame.image.load("media/start screen.jpg").convert_alpha()
imp = pygame.transform.smoothscale(imp, (860, 560))


def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.SysFont("Monoid", size)

def play():
        pygame.display.set_caption('your messy room😱')

        while True:
            SCREEN.fill("aliceblue")
            PLAY_MOUSE_POS = pygame.mouse.get_pos()


            PLAY_ROOM = pygame.image.load("media/room.jpg").convert_alpha()
            PLAY_ROOM = pygame.transform.smoothscale(PLAY_ROOM, (860, 560))
            SCREEN.blit(PLAY_ROOM, (40, 40))

            PLAY_BACK = Button(image=None, pos=(83, 22),
                           text_input="BACK", font=get_font(45), base_color="#a2a3bb", hovering_color="#b2d6b5")

            SETTINGS_BUTTON = Button(image=pygame.transform.smoothscale(pygame.image.load("media/settings button.png"), (29, 29)),
                pos=(164, 20),text_input=None, font=get_font(25), base_color="lightsalmon3", hovering_color="#b2d6b5")

            for button in [PLAY_BACK]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(SCREEN)

            for button in [SETTINGS_BUTTON]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(SCREEN)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        start_screen()
                    if SETTINGS_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        settings()

            pygame.display.update()

def info():
    pygame.display.set_caption('what is happening❓')
    while True:
        INFO_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("lightsalmon3")

        INFO_SCREEN = pygame.image.load("media/infopage.jpg").convert_alpha()
        INFO_SCREEN = pygame.transform.smoothscale(INFO_SCREEN, (860, 560))
        SCREEN.blit(INFO_SCREEN, (40, 40))

        INFO_BACK = Button(image=None, pos=(83, 22),
                           text_input="BACK", font=get_font(45), base_color="White", hovering_color="#b2d6b5")

        INFO_BACK.changeColor(INFO_MOUSE_POS)
        INFO_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INFO_BACK.checkForInput(INFO_MOUSE_POS):
                    start_screen()

        pygame.display.update()

def settings():
    pygame.display.set_caption('settings⚙️')
    SCREEN.fill("lightsalmon3")

    while True:

        SETTINGS_SCREEN = pygame.image.load("media/settingspage.png").convert_alpha()
        SETTINGS_SCREEN = pygame.transform.smoothscale(SETTINGS_SCREEN, (860, 560))
        SCREEN.blit(SETTINGS_SCREEN, (40, 40))

        SETTINGS_MOUSE_POS = pygame.mouse.get_pos()


        SETTINGS_BACK = Button(image=None, pos=(83, 22),
                           text_input="BACK", font=get_font(45), base_color="White", hovering_color="#b2d6b5")


        MUSIC_ON = Button(image=pygame.transform.smoothscale(pygame.image.load("media/music on button.png"), (80, 86)),
                          pos=(460, 330),
                          text_input="ON", font=get_font(25), base_color="white", hovering_color="black")

        MUSIC_OFF = Button(image=pygame.transform.smoothscale(pygame.image.load("media/music off button.png"), (80, 86)),
                          pos=(580, 330),
                          text_input="OFF", font=get_font(25), base_color="white", hovering_color="black")

        for button in [MUSIC_ON]:
            button.changeColor(SETTINGS_MOUSE_POS)
            button.update(SCREEN)

        for button in [MUSIC_OFF]:
            button.changeColor(SETTINGS_MOUSE_POS)
            button.update(SCREEN)

        for button in [SETTINGS_BACK]:
            button.changeColor(SETTINGS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MUSIC_ON.checkForInput(SETTINGS_MOUSE_POS):
                    pygame.mixer.music.play(-1)
                if MUSIC_OFF.checkForInput(SETTINGS_MOUSE_POS):
                    pygame.mixer.music.stop()
                if SETTINGS_BACK.checkForInput(SETTINGS_MOUSE_POS):
                    return()


        pygame.display.update()


# main menu/ start screen used from github: baraltech and adapted for my specific cases
def start_screen():
    pygame.display.set_caption('✨start screen✨')

    while True:
        SCREEN.fill('lightsalmon3')
        SCREEN.blit(imp, (40, 40))

        MENU_MOUSE_POS = pygame.mouse.get_pos()


        PLAY_BUTTON = Button(image=pygame.transform.smoothscale(pygame.image.load("media/play button.png"),(105,116)), pos=(570, 500),
                             text_input="PLAY", font=get_font(25), base_color="black", hovering_color="#b2d6b5")

        INFO_BUTTON = Button(image=pygame.transform.smoothscale(pygame.image.load("media/info button.png"), (40, 86)),
                             pos=(450, 500),
                             text_input="INFO", font=get_font(25), base_color="lightsalmon3", hovering_color="#b2d6b5")

        SETTINGS_BUTTON = Button(image=pygame.transform.smoothscale(pygame.image.load("media/settings button.png"), (79, 86)),
                             pos=(704, 500),
                             text_input="SETTINGS", font=get_font(25), base_color="lightsalmon3", hovering_color="#b2d6b5")

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for button in [INFO_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for button in [SETTINGS_BUTTON]:
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
                if SETTINGS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    settings()


        pygame.display.update()

start_screen()


'''
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
'''