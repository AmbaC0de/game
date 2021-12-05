import pygame

from projectile import Projectile


# Creation d'une premiere classe qui va representer le joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        self.game = game
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 6
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # Si le joueur n'a plus de points de vie
            self.game.game_over()

    def update_health_bar(self, surface):
        # Dessiner l'arriere plan de la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 6])
        # Dessiner la barre de vie
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 6])

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))  # on donne a Projectile() l'argument self pour recuperer
                                                    # les coordonnees du joueur et les attacher au projectile

    def move_right(self):
        # Le joueur pourra se déplacer que s'il n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
