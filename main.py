import pygame
import math
from game import Game
pygame.init()

################################################################################################
############################################# TUTO #############################################
###### https://www.youtube.com/watch?v=8J8wWxbAdFg&list=PLMS9Cy4Enq5KsM7GJ4LHnlBQKTQBV8kaR #####
################################################################################################
# définir une clock
clock = pygame.time.Clock()
FPS = 80

# générer la fenêtre du jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# importer l'image de l'arrière plan du jeu
background = pygame.image.load("assets/bg.jpg")

# importer la bannière pour la page d'accueil
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer le bouton pour lancer la partie
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 1.7)

# Charger notre jeu
game = Game()

running = True

# Boucle tant que cette condition est vrai
while running:
    # appliquer le background
    screen.blit(background, (0, -200))

    # vérifier si le jeu à commencer ou non
    if game.is_playing:
        # déclencher les instructions de la partie
        game.update(screen)
    else:
        # ajouter mon écran de bienvenue
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

    # mettre à jour l'écran
    pygame.display.flip()

    # Si le joueur ferme la fenêtre
    for event in pygame.event.get():
        # que l'évenement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # détecter si un joueur enclenche une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # détecter si la touche espace est déclenchée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # mettre le jeu en mode lancer
                    game.start()
                    # jouer le son du bouton
                    game.sound_manager.play("click") 
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérification pour savoir si la souris est en collision avec le bouton
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                game.start()
                # jouer le son du bouton
                game.sound_manager.play("click")
    # fixer le nb de fps sur la clock
    clock.tick(FPS)
