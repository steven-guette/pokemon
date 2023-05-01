import pygame as pg
from classes.projectile import Projectile
from classes.pokemon import Pokemon


class Water(Pokemon):
    def __init__(self, name, defense, attack, hit_points, is_player=False):
        super().__init__(name, hit_points, is_player)

        self.__type = "water"
        self.__defense = defense
        self.__attack = attack
        self.projectile = pg.sprite.GroupSingle()

    # region METHODS #######################

    def LoadProjectile(self):
        self.projectile = pg.sprite.GroupSingle(Projectile(self))

    # endregion ############################

    # region GETTERS #######################

    def GetType(self):
        return self.__type

    def GetDefense(self):
        return self.__defense

    def GetAttack(self):
        return self.__attack

    # endregion ############################
