import pygame
import random
import animation


# création de la classe qui gérera les monstres
class Monster(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.uniform(0.1, 1)
        self.start_animation()

    def damage(self, amount):
        # infliger des dégats
        self.health -= amount
        # vérifier si le nouveau nombre de point de vie est inférieur à zéro (décédé)
        if self.health <= 0:
            # le faire réapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.uniform(0.1, 1)
            self.health = self.max_health

            # si la barre d'évenement est à son maximum
            if self.game.comet_event.is_full_loaded():
                # retirer du jeu
                self.game.all_monsters.remove(self)
                # appel de la méthode pour déclencher la pluie de comète
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(True)

    def update_health_bar(self, surface):
        # définir une couleur pour la jauge de vie
        bar_color = (171, 243, 99)
        # définir une couleur pour l'arrière plan de la jauge
        back_bar_color = (60, 63, 60)

        # définir la position, largeur et épaisseur de la jauge de vie
        x = self.rect.x + 10
        y = self.rect.y - 20
        w = self.health
        h = 5
        bar_position = [x, y, w, h]
        # Définir la position de l'arrière plan de la jauge de vie
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # dessiner l'arrière plan de la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        # dessiner la barre de vie
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        # le déplacement ne se fait que s'il n'y a pas de collision avec un joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # Infliger des dégâts (au joueur)
            self.game.player.damage(self.attack)



