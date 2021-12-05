import pygame
from random import *


# Creation d'une classe qui va gerer la (les) monstres
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 600 + randint(0, 300)
        self.rect.y = 535
        self.velocity = randint(1, 4)

    def damage(self, amount):
        # Infliger des dégats au monstres
        self.health -= amount

        # Verifier si sa santé est egal a zero
        if self.health <= 0:
            # Faire reapparaitre le monstre
            self.rect.x = 1080 + randint(0, 300)
            self.velocity = randint(1, 4)
            self.health = self.max_health

    def update_health_bar(self, surface):

        # Dessiner l'arriere plan de la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 15, self.rect.y - 15, self.max_health, 5])
        # Dessiner la barre de vie
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 15, self.rect.y - 15, self.health, 5])

    def walk(self):
        # Le déplacement ne pourra se faire que s'il n'y pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
