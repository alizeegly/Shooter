import pygame
import random

# définir une class qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    # définir les choses à faire lors de la création de l'entité
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load('assets/' + sprite_name + '.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 # commencer l'animation à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # definir une methode pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    # definir une méthode pour animer le sprite
    def animate(self, loop=False):
        # vérifier si l'animation est active
        if self.animation:
            # passer à l'image suivante
            self.current_image += random.randint(0, 1)
            # vérifier si on atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au départ
                self.current_image = 0
                # vérifier si l'animation n'est pas en mode loop
                if loop is False:
                    # désactivation de l'animation
                    self.animation = False
            # modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

# Définir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les 24 images de sprite dans le dossier correspondant
    images = []
    # récupérer le chemin du dossier pour le sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque fichiers / images du dossier
    for num in range(2, 24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    return images

# Définir un dictionnaire qui va contenir les images chargées de chaque sprite
animations = {
    'mummy': load_animation_images("mummy"),
    'player': load_animation_images("player"),
    'alien': load_animation_images("alien"),
}