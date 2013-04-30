import pygame

class Shot(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/images/shot.png")
        self.sound = pygame.mixer.Sound("assets/sounds/shot.wav")
        self.playSound()
        self.x = player.getCoordinates()[0] + player.returnImage().get_width() / 2 -3
        self.y = screen.get_height() - player.returnImage().get_height()
        self.rect=self.image.get_rect()
        self.rect.center = self.getCoordinates()

    def returnImage(self):
        return self.image

    def update(self):
        # move the shot before displaying it
        self.moveShot()
        # check if it can be seen
        if self.y < 0:
            return True
        # draw bullet if it can be seen
        self.rect.center = self.getCoordinates()

    def moveShot(self):
        self.y -= 10

    def getCoordinates(self):
        return (self.x - self.image.get_width() -4, self.y)

    def playSound(self):
        self.sound.play()