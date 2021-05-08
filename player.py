import pygame
from projectile import Projectile
import animation

# création de la class Joueur
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        # création de la nouvelle instance de la classe Projectile
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)
        # démarrer l'animation
        self.start_animation()
        self.game.sound_manager.play('tir')

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # définir une couleur pour la jauge de vie
        bar_color = (171, 243, 99)
        # définir une couleur pour l'arrière plan de la jauge
        back_bar_color = (60, 63, 60)

        # définir la position, largeur et épaisseur de la jauge de vie
        x = self.rect.x + 50
        y = self.rect.y + 15
        w = self.health
        h = 7
        bar_position = [x, y, w, h]
        # Définir la position de l'arrière plan de la jauge de vie
        back_bar_position = [self.rect.x + 50, self.rect.y + 15, self.max_health, 7]

        # dessiner l'arrière plan de la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # dessiner la barre de vie
        pygame.draw.rect(surface, bar_color, bar_position)

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de point de vie
            self.game.game_over()
