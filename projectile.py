import pygame


# Définition de la class qui va gérer les projectiles lancés par le joueur
class Projectile(pygame.sprite.Sprite):  # la classe Projectile est une classe enfant qui hérite de la super classe Sprite() de pygame

    # Definition du constructeur __init__() de la classse Projectile
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 8
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # Faire tourner le projectile
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove_projectile(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # Verifier si le projectile entre en collision avec un monstre
        for monster in  self.player.game.check_collision(self, self.player.game.all_monsters):
            # Supprimer le projectile
            self.remove_projectile()
            # Infliger des degats au monstres
            monster.damage(self.player.attack)

        # Si le projectile quitte l'ecran, le detruire
        if self.rect.x > 1080:
            self.remove_projectile()
