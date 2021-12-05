import pygame

from monster import Monster
from player import Player


# Création classe qui va representer le jeu
class Game:
    
    def __init__(self):
        # Ajout d'une proprité qui va definir si le jeu a demarer
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)  # Chargement du joueur dès qu'une partie est crée
        self.all_players.add(self.player)
        self.pressed = {}
        self.all_monsters = pygame.sprite.Group()  # Groupe de monstres

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # Recommencer une nouvelle partie
        self.all_monsters = pygame.sprite.Group()
        # print(self.player.health)
        self.player.health = self.player.max_health
        self.is_playing = False

    def update_game(self, screen):
        # Appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # Récuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Récuperer les monstres du jeu et mettre a jour leur barre de vie
        for monster in self.all_monsters:
            monster.walk()
            monster.update_health_bar(screen)

        # Afficher et mettre a jour la barre de vie du joueur
        self.player.update_health_bar(screen)

        # Appliquer l'ensemble des images du groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # Appliquer l'ensemble des images du groupe de monstres
        self.all_monsters.draw(screen)

        # Verifier si le joueur veut aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
