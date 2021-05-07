import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent


# création de la class Jeu
class Game:

    def __init__(self):
        # Définir si le jeu à commencer ou non
        self.is_playing = False
        # Charger un joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # générer l'evenement de la pluie de comètes
        self.comet_event = CometFallEvent(self)
        # Groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def update(self, screen):
        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser la barre d'évenement du jeu
        self.comet_event.update_bar(screen)

        # récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # récupérer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # récupérer les cometes
        for comete in self.comet_event.all_cometes:
            comete.fall()

        # appliquer l'ensemble des images du groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images du groupe de monstres
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des images du groupe de comètes
        self.comet_event.all_cometes.draw(screen)

        # vérifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x >= 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def game_over(self):
        # remettre le jeu à neuf, retirer les monstres, remettre le joueur à 100 de vie et mettre le jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_cometes = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()