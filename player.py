import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("assets/images/player.png"), (32,32))
        self.y = screen.get_height() - self.image.get_height()
        self.x = screen.get_width() / 2 - self.image.get_width() / 2
        self.maxScreen = screen.get_width()
        self.rect=self.image.get_rect()
        self.rect.center = self.getCoordinates()

    def returnImage(self):
        return self.image

    def getCoordinates(self):
        return (self.x + self.image.get_width() / 2, self.y)

    def moveVertically(self, movement):
        # check if movement would make the ship move out of screen, if not do the move
        if self.x + movement > 0 and self.x + movement < self.maxScreen - self.image.get_width() / 2 - 10:
            self.x += movement

    def update(self):
        self.rect.center = self.getCoordinates()
