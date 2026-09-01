import pygame, sys
from button import Button

# pygame setup
pygame.init()

X = 900
Y = 600
SCREEN = pygame.display.set_mode((X, Y))

# filling the screen with a color
SCREEN.fill('lightsalmon3')

# set the pygame window name
pygame.display.set_caption('✨declutter your mind✨')

#including sound into my game
pygame.mixer.music.load('media/music.mp3')
pygame.mixer.music.play(-1)


# flip() the display to put your work on screen
pygame.display.flip()


# create a surface object, image is drawn on it.
imp = pygame.image.load("media/startscreen.jpg").convert_alpha()
imp = pygame.transform.scale(imp, (860, 560))


SCREEN.blit(imp, (20, 20))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.SysFont("Arial", size)

def play():
    pygame.display.set_caption('✨your messy room✨')
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("lightsalmon3")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

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


# main menu/ start screen used from github: baraltech and adapted for my specific cases
def start_screen():
    pygame.display.set_caption('✨start screen✨')


    while True:
        SCREEN.blit(imp, (20, 20))

        MENU_MOUSE_POS = pygame.mouse.get_pos()


        PLAY_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("media/play button.png"),(155,196)), pos=(464, 450),
                             text_input="PLAY", font=get_font(25), base_color="lightsalmon3", hovering_color="White")


        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                    sys.exit()

        pygame.display.update()

start_screen()


'''
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
'''