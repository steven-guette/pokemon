import pygame as pg


class Projectile(pg.sprite.Sprite):
    def __init__(self, pokemon):
        super().__init__()

        self.pokemon = pokemon
        self.velocity = 4
        self.image = pg.image.load(f"resources/images/projectiles/{pokemon.GetType()}.png")
        self.rect = self.image.get_rect()
        self.SetRect()

    # region METHODS ####################

    def MoveRight(self):
        self.rect.x += self.velocity

    def MoveLeft(self):
        self.rect.x -= self.velocity

    # endregion #########################

    # region SETTERS ####################

    def SetRect(self):
        if self.pokemon.isPlayer:
            self.rect.x = self.pokemon.rect.x + self.pokemon.rect.width
        else:
            self.rect.x = self.pokemon.rect.x - self.pokemon.rect.width / 2

        self.rect.y = self.pokemon.rect.y + 25

    # endregion #########################
