import pygame, sys, os
from button import Button
from mess import Mess

# pygame setup
pygame.init()

X = 940
Y = 640
SCREEN = pygame.display.set_mode((X, Y))

#preloading the music and adjusting the volume
pygame.mixer.music.load('media/music.mp3')
pygame.mixer.music.set_volume(1.0)
clicksound = pygame.mixer.Sound('media/buttonclick.mp3')
clicksound.set_volume(0.6)
mess_clicksound = pygame.mixer.Sound('media/messclick.mp3')

# setting the pygame window name
pygame.display.set_caption('✨declutter your mind✨')

# creating a surface object with start screen drawn on it.
imp = pygame.image.load("media/start screen.jpg").convert_alpha()
imp = pygame.transform.smoothscale(imp, (860, 560))


def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.SysFont("Monoid", size)

def play():
        pygame.display.set_caption('your messy room😱')

        PLAY_ROOM = pygame.image.load("media/room.jpg").convert_alpha()
        PLAY_ROOM = pygame.transform.smoothscale(PLAY_ROOM, (860, 560))

        font = pygame.font.SysFont('Arial', 15, 'bold')
        score = 0
        BLACK = (0, 0, 0)

        #setting the different Buttons that are shown on the screen


        PLAY_BACK = Button(image=None, pos=(83, 22),
                           text_input="BACK", font=get_font(45), base_color="#a2a3bb", hovering_color="#b2d6b5")

        SETTINGS_BUTTON = Button(
            image=pygame.transform.smoothscale(pygame.image.load("media/settings button.png"), (29, 29)),
            pos=(164, 20), text_input=None, font=get_font(25), base_color="lightsalmon3", hovering_color="#b2d6b5")

        INFO_BUTTON = Button(image=pygame.transform.smoothscale(pygame.image.load("media/info button.png"), (16, 30)),
                             pos=(204, 20), text_input=None, font=get_font(25), base_color="lightsalmon3",
                             hovering_color="#b2d6b5")

        mess1 = Mess('media/mess1.png', 204, 20)
        '''mess2 =
        mess3 =
        mess4 =
        '''
        all_sprites = pygame.sprite.Group()
        all_sprites.add(mess1)


        while True:
            SCREEN.fill("aliceblue")
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.blit(PLAY_ROOM, (40, 40))

            for button in [PLAY_BACK]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(SCREEN)

            for button in [SETTINGS_BUTTON]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(SCREEN)

            for button in [INFO_BUTTON]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        clicksound.play()
                        return()
                    if SETTINGS_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        clicksound.play()
                        settings()
                    if INFO_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        clicksound.play()
                        info()
                    for sprite in all_sprites:
                        if sprite.rect.collidepoint(event.pos):
                            mess_clicksound.play()
                            score += 1
                            sprite.kill()


            all_sprites.update()
            all_sprites.draw(SCREEN)

            score_text = font.render(f"Score: {score}", True, BLACK)
            SCREEN.blit(score_text, (10, 10))

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
                    clicksound.play()
                    return()

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
                    clicksound.play()
                    pygame.mixer.music.play(-1)
                if MUSIC_OFF.checkForInput(SETTINGS_MOUSE_POS):
                    clicksound.play()
                    pygame.mixer.music.stop()
                if SETTINGS_BACK.checkForInput(SETTINGS_MOUSE_POS):
                    clicksound.play()
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
                    clicksound.play()
                    play()
                if INFO_BUTTON.checkForInput(MENU_MOUSE_POS):
                    clicksound.play()
                    info()
                if SETTINGS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    clicksound.play()
                    settings()


        pygame.display.update()

def main():

    start_screen()

if __name__ == '__main__':
    main()

