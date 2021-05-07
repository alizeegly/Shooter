import pygame

# définir une class qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    # définir les choses à faire lors de la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load('assets/' + sprite_name + '.png')
