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
mess_clicksound.set_volume(0.3)
# setting the pygame window name
pygame.display.set_caption('✨declutter your mind✨')

# creating a surface object with start screen drawn on it.
imp = pygame.image.load("media/start screen.jpeg").convert_alpha()
imp = pygame.transform.smoothscale(imp, (860, 560))


def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.SysFont("Monoid", size)

def play():
        pygame.display.set_caption('your messy room😱')

        play_room = pygame.image.load("media/room.jpg").convert_alpha()
        play_room = pygame.transform.smoothscale(play_room, (860, 560))

        score_block = pygame.image.load("media/score.png").convert_alpha()
        score_block = pygame.transform.smoothscale(score_block, (153, 50))

        game_over = pygame.image.load('media/gameover.png')
        game_over = pygame.transform.smoothscale(game_over,(860, 590))

        font_score = pygame.font.SysFont('Monoid',36 )
        font_message = pygame.font.SysFont ('Monoid', 30)
        score = 0

        #setting the different Buttons that are shown on the screen


        play_back = Button(image=pygame.transform.smoothscale(pygame.image.load("media/back button.png"),(120, 59)), pos=(96, 22),
                           text_input=None, font=get_font(45), base_color="#a2a3bb", hovering_color="#b2d6b5")

        settings_button = Button(
            image=pygame.transform.smoothscale(pygame.image.load("media/settings button.png"), (29, 29)),
            pos=(164, 20), text_input=None, font=get_font(25), base_color="lightsalmon3", hovering_color="#b2d6b5")

        info_button = Button(image=pygame.transform.smoothscale(pygame.image.load("media/info button.png"), (16, 30)),
                             pos=(204, 20), text_input=None, font=get_font(25), base_color="lightsalmon3",
                             hovering_color="#b2d6b5")

        half_way_text = font_message.render("you are doing great :)", True, '#313030')
        motivation_text = font_message.render("try again :)", True, '#313030')
        text_rect = pygame.Rect(400, 260, 220, 35)
        motivation_rect = pygame.Rect(400, 260, 120, 35)
        play_room_rect = play_room.get_rect(topleft=(40, 40))

        mess1 = Mess('media/mess1.png', 644, 480, 60,60)
        mess2 = Mess('media/mess2.png', 294, 250, 100, 150)
        mess3 = Mess('media/mess3.png', 304, 430, 210, 110)
        mess4 = Mess('media/mess4.png', 504, 420, 100, 120)
        mess5 = Mess('media/mess5.png', 444, 356, 140, 60)
        mess6 = Mess('media/mess6.png', 174, 440, 125, 175)
        mess7 = Mess('media/mess7.png', 487, 120, 70, 90)
        mess8 = Mess('media/mess8.png', 574, 390, 40, 45)
        mess9 = Mess('media/mess9.png', 364, 99, 60, 75)
        mess10 = Mess('media/mess10.png', 800, 412, 80, 109)
        mess11 = Mess('media/mess11.png', 360, 400, 120,60)
        mess12 = Mess('media/mess12.png', 542, 490, 80, 130)
        mess13 = Mess('media/mess13.png', 626, 425, 35, 30)

        all_sprites = pygame.sprite.Group()
        all_sprites.add(mess1, mess2, mess3, mess4, mess5, mess6, mess7, mess8, mess9, mess10, mess11, mess12, mess13)

        play_button = Button(
            image=pygame.transform.smoothscale(pygame.image.load("media/play button.png"), (89, 100)),
            pos=(855, 570),
            text_input="play again", font=get_font(25), base_color='#fcfc84', hovering_color="#313030")

        # E3E0DD
        while True:
            screen.fill("#e3dcce")

            play_mouse_pos = pygame.mouse.get_pos()

            screen.blit(play_room, (40, 40))
            screen.blit(score_block,(733, 50))

            all_sprites.update()
            all_sprites.draw(screen)
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

                    if play_room_rect.collidepoint(event.pos):

                        for sprite in all_sprites:
                            if sprite.rect.collidepoint(event.pos):
                                mess_clicksound.play()
                                score += 1
                                sprite.kill()
                                break
                        else:
                            clicksound.play()
                            pygame.draw.rect(screen, "#ECE26F", motivation_rect, border_radius=6)
                            screen.blit(motivation_text, (407, 267))
                            pygame.display.update()
                            pygame.time.delay(800)

            score_text = font_score.render(f"{score}", True, '#313030')
            screen.blit(score_text, (850, 60))


            if score == 5:
                pygame.draw.rect(screen, "#A2DDDE", text_rect, border_radius=6)
                screen.blit(half_way_text, (407,267))
                pygame.display.update()


            if score == 11:

                all_sprites.empty()

                pygame.display.set_caption('✨✨✨')
                pygame.display.update()
                screen.fill("lightsalmon3")
                screen.blit(game_over,(40,40))


                play_button.update(screen)
                play_button.changeColor(play_mouse_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(play_mouse_pos):
                        clicksound.play()
                        play()

                        all_sprites.update()
                        all_sprites.draw(screen)


            pygame.display.update()

def info():
    pygame.display.set_caption('what is happening❓')


    info_back = Button(image=pygame.transform.smoothscale(pygame.image.load("media/back button.png"),(120, 59)), pos=(83, 22),
                       text_input=None, font=get_font(45), base_color="White", hovering_color="#b2d6b5")

    while True:
        screen.fill("lightsalmon3")

        info_mouse_pos = pygame.mouse.get_pos()
        info_back.changeColor(info_mouse_pos)
        info_back.update(screen)

        info_screen = pygame.image.load("media/infopage.jpg").convert_alpha()
        info_screen = pygame.transform.smoothscale(info_screen, (860, 560))
        screen.blit(info_screen, (40, 40))


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

    while True:
        screen.fill("lightsalmon3")

        settings_screen = pygame.image.load("media/settingspage.png").convert_alpha()
        settings_screen = pygame.transform.smoothscale(settings_screen, (860, 560))
        screen.blit(settings_screen, (40, 40))

        settings_mouse_pos = pygame.mouse.get_pos()


        settings_back = Button(image=pygame.transform.smoothscale(pygame.image.load("media/back button.png"),(120, 59)), pos=(83, 22),
                           text_input=None, font=get_font(45), base_color="White", hovering_color="#b2d6b5")


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
                             text_input="PLAY", font=get_font(25), base_color='#313030', hovering_color="#b2d6b5")

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

