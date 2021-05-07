import pygame
from comet import Comet


# Création de la classe qui gérera la chute de comète
class CometFallEvent:

    # lors du chargement, création d'un compteur
    def __init__(self, game):
        self.percent = 0
        self.percente_speed = 5
        self.game = game
        self.fall_mode = False

        # Définir un groupe de sprite pour stocker les comètes
        self.all_cometes = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percente_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # boucle pour faire apparaître 10 boules de feu
        for i in range(1, 10):
            # faire apparaître une boule de feu
            self.all_cometes.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'évenement est totalement chargée
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True  # activer l'évenement

    def update_bar(self, surface):
        # ajouter du pourcentage à la barre
        self.add_percent()
        # barre noire en arrière plan
        pygame.draw.rect(surface, (60, 63, 60), [0, surface.get_height()-20, surface.get_width(), 10])
        # barre rouge d'event
        pygame.draw.rect(surface, (187, 11, 11), [0, surface.get_height()-20, (surface.get_width() / 100) * self.percent, 10])
