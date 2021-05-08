import pygame
import random


# classe pour générer une comète
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_cometes.remove(self)
        self.comet_event.game.sound_manager.play("meteorite")

        # vérifier si le nombre de comètes est de 0
        if len(self.comet_event.all_cometes) == 0:
            print("l'évenement est finie")
            # remettre la barre à 0
            self.comet_event.reset_percent
            # faire apparaître les 2 premiers monstres
            # self.comet_event.game.spawn_monster(Mummy)
            # self.comet_event.game.spawn_monster(Alien)
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            print("Sol")
            self.remove()
            # si il y a plus de boules de feu
            if len(self.comet_event.all_cometes) == 0:
                print("L'évenement est fini")
                # remetre la jauge de vie au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # vérifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            print("Joueur touché !")
            self.remove()
            # subir 20 points de dégats
            self.comet_event.game.player.damage(20 )
