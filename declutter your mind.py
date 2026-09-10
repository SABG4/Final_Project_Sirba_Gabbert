import pygame, sys, os
from button import Button
from mess import Mess

# pygame setup
pygame.init()

X = 940
Y = 640
screen = pygame.display.set_mode((X, Y))

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

        play_room = pygame.image.load("media/room.jpg").convert_alpha()
        play_room = pygame.transform.smoothscale(play_room, (860, 560))

        tidied_room = pygame.image.load('media/tidiedroom.jpg')
        tidied_room = pygame.transform.smoothscale(tidied_room, (860, 560))

        game_over = pygame.image.load()
        game_over = pygame.transform.smoothscale()

        font = pygame.font.SysFont('Monoid', 35, )
        score = 0
        BLACK = (0, 0, 0)

        #setting the different Buttons that are shown on the screen


        play_back = Button(image=None, pos=(83, 22),
                           text_input="BACK", font=get_font(45), base_color="#a2a3bb", hovering_color="#b2d6b5")

        settings_button = Button(
            image=pygame.transform.smoothscale(pygame.image.load("media/settings button.png"), (29, 29)),
            pos=(164, 20), text_input=None, font=get_font(25), base_color="lightsalmon3", hovering_color="#b2d6b5")

        info_button = Button(image=pygame.transform.smoothscale(pygame.image.load("media/info button.png"), (16, 30)),
                             pos=(204, 20), text_input=None, font=get_font(25), base_color="lightsalmon3",
                             hovering_color="#b2d6b5")

        mess1 = Mess('media/mess1.png', 224, 460, 80,80)
        '''mess2 =
        mess3 =
        mess4 =
        mess5 =
        mess6 =
        mess7 =
        mess8 =
        mess9 =
        mess10 =
'''
        all_sprites = pygame.sprite.Group()
        all_sprites.add(mess1)


        while True:
            screen.fill("aliceblue")
            play_mouse_pos = pygame.mouse.get_pos()

            screen.blit(play_room, (40, 40))

            for button in [play_back]:
                button.changeColor(play_mouse_pos)
                button.update(screen)

            for button in [settings_button]:
                button.changeColor(play_mouse_pos)
                button.update(screen)

            for button in [info_button]:
                button.changeColor(play_mouse_pos)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_back.checkForInput(play_mouse_pos):
                        clicksound.play()
                        return()
                    if settings_button.checkForInput(play_mouse_pos):
                        clicksound.play()
                        settings()
                    if info_button.checkForInput(play_mouse_pos):
                        clicksound.play()
                        info()
                    for sprite in all_sprites:
                        if sprite.rect.collidepoint(event.pos):
                            mess_clicksound.play()
                            score += 1
                            sprite.kill()

            if score == 1:
                screen.blit(tidied_room, (40, 40))

            if score == 10:
                screen.blit(game_over,(40,40))


            all_sprites.update()
            all_sprites.draw(screen)

            score_text = font.render(f"Score: {score}", True, BLACK)
            screen.blit(score_text, (823, 50))

            pygame.display.update()

def info():
    pygame.display.set_caption('what is happening❓')
    while True:
        info_mouse_pos = pygame.mouse.get_pos()

        screen.fill("lightsalmon3")

        info_screen = pygame.image.load("media/infopage.jpg").convert_alpha()
        info_screen = pygame.transform.smoothscale(info_screen, (860, 560))
        screen.blit(info_screen, (40, 40))

        info_back = Button(image=None, pos=(83, 22),
                           text_input="BACK", font=get_font(45), base_color="White", hovering_color="#b2d6b5")

        info_back.changeColor(info_mouse_pos)
        info_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if info_back.checkForInput(info_mouse_pos):
                    clicksound.play()
                    return()

        pygame.display.update()

def settings():
    pygame.display.set_caption('settings⚙️')
    screen.fill("lightsalmon3")

    while True:

        settings_screen = pygame.image.load("media/settingspage.png").convert_alpha()
        settings_screen = pygame.transform.smoothscale(settings_screen, (860, 560))
        screen.blit(settings_screen, (40, 40))

        settings_mouse_pos = pygame.mouse.get_pos()


        settings_back = Button(image=None, pos=(83, 22),
                           text_input="BACK", font=get_font(45), base_color="White", hovering_color="#b2d6b5")


        music_on = Button(image=pygame.transform.smoothscale(pygame.image.load("media/music on button.png"), (80, 86)),
                          pos=(460, 330),
                          text_input="ON", font=get_font(25), base_color="white", hovering_color="black")

        music_off = Button(image=pygame.transform.smoothscale(pygame.image.load("media/music off button.png"), (80, 86)),
                          pos=(580, 330),
                          text_input="OFF", font=get_font(25), base_color="white", hovering_color="black")

        for button in [music_on]:
            button.changeColor(settings_mouse_pos)
            button.update(screen)

        for button in [music_off]:
            button.changeColor(settings_mouse_pos)
            button.update(screen)

        for button in [settings_back]:
            button.changeColor(settings_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if music_on.checkForInput(settings_mouse_pos):
                    clicksound.play()
                    pygame.mixer.music.play(-1)
                if music_off.checkForInput(settings_mouse_pos):
                    clicksound.play()
                    pygame.mixer.music.stop()
                if settings_back.checkForInput(settings_mouse_pos):
                    clicksound.play()
                    return()


        pygame.display.update()

# main menu/ start screen used from github: baraltech and adapted for my specific cases
def start_screen():
    pygame.display.set_caption('✨start screen✨')

    while True:
        screen.fill('lightsalmon3')
        screen.blit(imp, (40, 40))

        menu_mouse_pos = pygame.mouse.get_pos()


        play_button = Button(image=pygame.transform.smoothscale(pygame.image.load("media/play button.png"),(105,116)), pos=(570, 500),
                             text_input="PLAY", font=get_font(25), base_color="black", hovering_color="#b2d6b5")

        info_button = Button(image=pygame.transform.smoothscale(pygame.image.load("media/info button.png"), (40, 86)),
                             pos=(450, 500),
                             text_input="INFO", font=get_font(25), base_color="lightsalmon3", hovering_color="#b2d6b5")

        settings_button = Button(image=pygame.transform.smoothscale(pygame.image.load("media/settings button.png"), (79, 86)),
                             pos=(704, 500),
                             text_input="SETTINGS", font=get_font(25), base_color="lightsalmon3", hovering_color="#b2d6b5")

        for button in [play_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for button in [info_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for button in [settings_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    clicksound.play()
                    play()
                if info_button.checkForInput(menu_mouse_pos):
                    clicksound.play()
                    info()
                if settings_button.checkForInput(menu_mouse_pos):
                    clicksound.play()
                    settings()


        pygame.display.update()

def main():

    start_screen()

if __name__ == '__main__':
    main()

