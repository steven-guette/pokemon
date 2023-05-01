import pygame as pg
from classes.whiteshield import WShield
from classes.commentbox import CommentBox


class Pokemon(pg.sprite.Sprite):
    def __init__(self, name, hit_points, is_player):
        super().__init__()

        self.isPlayer = is_player
        self.__name = name
        self.__hpMax = hit_points
        self.__hp = self.__hpMax
        self.commentGroup = pg.sprite.Group()
        self.velocity = 5
        self.image = pg.image.load(f"resources/images/pokemons/{name}.png")
        self.rect = self.image.get_rect()

    # region METHODS #################

    def TakeDamage(self, damage):
        if self.__hp - damage >= 0:
            self.__hp -= damage
        else:
            self.__hp = 0

    def Advance(self):
        self.rect.x += self.velocity

    def MoveBack(self):
        self.rect.x -= self.velocity

    def AddComment(self, comment):
        self.commentGroup.add(CommentBox(self, comment))

    # endregion ######################

    # region SETTERS #################

    def SetHitPointsBar(self, surface):
        borderColor = (0, 0, 0)
        barColor = (255, 99, 71)

        borderPosition = [self.rect.x - 20, self.rect.y - 21, self.__hpMax + 2, 7]
        barPosition = [self.rect.x - 19, self.rect.y - 20, self.__hp, 5]

        pg.draw.rect(surface, borderColor, borderPosition, 0, 5)
        pg.draw.rect(surface, barColor, barPosition, 0, 5)

    def SetRectPosition(self, x, y):
        if WShield.IsNumeric(x) and WShield.IsNumeric(y):
            self.rect.x = x
            self.rect.y = y

    # endregion ######################

    # region GETTERS #################

    def GetName(self):
        return self.__name

    def GetHitPoints(self):
        return self.__hp

    # endregion ######################
