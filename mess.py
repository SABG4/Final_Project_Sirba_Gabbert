import pygame

class Mess(pygame.sprite.Sprite):

    def __init__(self, image, x,y, width,height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.transform.smoothscale(pygame.image.load(image), (width,height))

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y

