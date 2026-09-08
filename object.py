import pygame

class TodoSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Load image
        self.image = pygame.image.load("media/todoliste.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (175, 175))

        # Set position
        self.rect = self.image.get_rect(topleft=(x, y))

        # Score
        self.score = 0

    def update(self, mouse_pos):
        # Check if clicked
        if self.rect.collidepoint(mouse_pos):
            self.score += 1
            print(f"Score: {self.score}")
            # Optional: Play sound
            # clicksound.play()