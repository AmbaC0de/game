import pygame

from game import Game

import math

pygame.init()

# Génération de la fenetre du jeu
pygame.display.set_caption("Comet fall game")  # display permet de gerer l'affichage du jeu; set_caption() permet de changer le titre de la fenetre de meme que l'icone

screen = pygame.display.set_mode((1080, 720))  # la méthode set_mode() permet de definir la taille de la fenetre

# Importation de l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')

# Importation de la baniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.floor(screen.get_width() / 4)

# Importation du buton de lancement de la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.floor(screen.get_width() / 3.33)
play_button_rect.y = math.floor(screen.get_height() / 1.93)

# Chargement du jeu
game = Game()

running = True

# BOUCLE DU JEU
while running:

    # APPLIQUER L'ARRIERE PLAN DU JEU
    screen.blit(background, (0, -200))  # blit() permet d'injecter une image à un endroit specifique de la fenetre

    # VERIFIER SI LE JEU COMMENCE OU PAS
    if game.is_playing:
        # Lancer la partie
        game.update_game(screen)
    # Verifier si le jeu n'a pas commencé
    else:
        # Ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # Mis a jour de l'ecran
    pygame.display.flip()  # La fonction flip() permet de mettre a jour la fenetre

    for event in pygame.event.get():
        # Verifier si l'évenement est fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # print('fermeture du jeu')
        # Detecter si un joueur lache une touche du clavier

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # Detecter si la touche espace est appuyé pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verification pour savoir si la souris est en collisition avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # Lancer la partie
                # print('clique détecté')
                game.start()
