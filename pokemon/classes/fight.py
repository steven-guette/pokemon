import pygame as pg
from time import sleep
from random import randint
from math import ceil

from classes.jsonfile import JSONFile
from classes.pokedex import Pokedex
from classes.electric import Electric
from classes.water import Water
from classes.grass import Grass
from classes.fire import Fire
from classes.normal import Normal

fightPower = JSONFile("resources/datas/fight_power.json", False)


class Fight:
    IsPlaying = False
    IsSelected = False
    ReadyToFight = False
    FightIsEnd = False

    def __init__(self, screen):
        self.Area = screen
        self.pokedex = Pokedex()
        self.pokemonPower = fightPower.GetContent(True)
        self.clock = pg.time.Clock()

        self.Winner = ""
        self.Player = Fight.GetPokemonSelected(self.pokedex.GetPokemonByName("pikachu"))
        self.Enemy = Fight.GetPokemonSelected(self.pokedex.GetPokemonByName("pikachu"))
        self.FightersGroup = pg.sprite.Group()
        self.PokemonsGroup = list()

        self.SetPokemonsGroup()

    def FightersWalks(self):
        if self.Player.rect.x < (self.Area.get_width() / 4 - self.Player.rect.width / 2):
            sleep(0.03)
            self.Player.Advance()
            self.Enemy.MoveBack()
        else:
            self.ReadyToFight = True

    def LaunchProjectile(self, From, To):
        if self.ReadyToFight:
            self.Player.SetHitPointsBar(self.Area)
            self.Enemy.SetHitPointsBar(self.Area)

            if not From.projectile:
                From.LoadProjectile()

            From.projectile.draw(self.Area)

            for comment in To.commentGroup:
                self.Area.blit(comment.text, comment.textRect)
                comment.MoveUp()

            sleep(0.01)

            for p in From.projectile:
                if From.rect.x > To.rect.x:
                    p.MoveLeft()
                else:
                    p.MoveRight()

                if self.CheckCollision(p, self.FightersGroup):
                    rand = randint(0, 5)

                    if rand > 2:
                        damage = self.pokemonPower[From.GetType()][To.GetType()] * From.GetAttack()

                        if rand == 5:
                            damage *= 1.5
                            To.AddComment(f"Crit ! -{ceil(damage)} hp")
                        else:
                            To.AddComment(f"-{ceil(damage)} hp")

                        To.TakeDamage(damage)
                    else:
                        To.AddComment("Esquive !")

                    p.kill()

                    if To.GetHitPoints() <= 0:
                        if From.GetHitPoints() > 0:
                            self.Winner = From.GetName()

                        self.EndFight()

    def EndFight(self):
        self.IsSelected = False
        self.IsPlaying = False
        self.ReadyToFight = False
        self.FightIsEnd = True

        for fighter in self.FightersGroup:
            fighter.kill()

    def CheckCollision(sprite, group):
        return pg.sprite.spritecollide(sprite, group, False)

    CheckCollision = staticmethod(CheckCollision)

    # region SETTERS #######################

    def SetPokemonsGroup(self):
        pokemonList = self.pokedex.GetPokemonsList()

        if len(pokemonList) > 0:
            xMargin = 55
            yPosition = self.Area.get_height() / 2
            xPosition = xMargin

            for pokemon in pokemonList:
                image = pg.image.load(f"resources/images/pokemons/{pokemon['name']}.png")
                imageRect = image.get_rect()

                imageRect.x = xPosition
                imageRect.y = yPosition - imageRect.height / 2
                xPosition += imageRect.width + xMargin

                self.PokemonsGroup.append({"name": pokemon["name"], "img": image, "rect": imageRect})

    def SetFighters(self, playerSelection):
        self.Player = self.GetPokemonSelected(playerSelection, True)
        self.Enemy = self.GetRandomPokemon()

        self.Player.IsPlayer = True

        self.Player.SetRectPosition(0 - self.Player.rect.width * 2,
                                    self.Area.get_height() / 2 - self.Player.rect.height / 2)
        self.Enemy.SetRectPosition(self.Area.get_width() + self.Enemy.rect.width,
                                   self.Area.get_height() / 2 - self.Enemy.rect.height / 2)

        self.FightersGroup.add(self.Player)
        self.FightersGroup.add(self.Enemy)

    # endregion ############################

    # region GETTERS #######################

    def GetPokemonSelected(pokemon, is_player=False):
        match pokemon["type"]:
            case "electric":
                return Electric(pokemon["name"], pokemon["defense"], pokemon["attack"], pokemon["hp"], is_player)
            case "water":
                return Water(pokemon["name"], pokemon["defense"], pokemon["attack"], pokemon["hp"], is_player)
            case "fire":
                return Fire(pokemon["name"], pokemon["defense"], pokemon["attack"], pokemon["hp"], is_player)
            case "grass":
                return Grass(pokemon["name"], pokemon["defense"], pokemon["attack"], pokemon["hp"], is_player)
            case _:
                return Normal(pokemon["name"], pokemon["defense"], pokemon["attack"], pokemon["hp"], is_player)

    GetPokemonSelected = staticmethod(GetPokemonSelected)

    def GetRandomPokemon(self):
        return self.GetPokemonSelected(self.pokedex.GetPokemonByID(randint(0, len(self.pokedex.GetPokemonsList())-1)))

    # endregion ############################
