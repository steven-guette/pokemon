import pygame as pg


def FightStart(screen, Game):
    imageVersus = pg.image.load("resources/images/versus_logo.png")
    imageVersus = pg.transform.scale(imageVersus, (90, 90))

    font = pg.font.SysFont("Comic Sans MS", 36, True)

    pokemonLeftName = font.render(Game.Player.GetName().capitalize(), True, (254, 163, 40))
    pokemonRightName = font.render(Game.Enemy.GetName().capitalize(), True, (32, 111, 185))

    screen.blit(imageVersus, (screen.get_width()/2 - imageVersus.get_width()/2, 10))
    screen.blit(pokemonLeftName, (screen.get_width()/4 - pokemonLeftName.get_width()/2, 20))
    screen.blit(pokemonRightName, (screen.get_width() - screen.get_width()/4 - 70, 20))

    screen.blit(Game.Player.image, Game.Player.rect)
    screen.blit(Game.Enemy.image, Game.Enemy.rect)

    Game.FightersWalks()

    Game.LaunchProjectile(Game.Player, Game.Enemy)
    Game.LaunchProjectile(Game.Enemy, Game.Player)
