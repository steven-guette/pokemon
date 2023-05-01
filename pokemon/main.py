import pygame as pg

from classes.fight import Fight

import includes.main_menu as main_menu
import includes.pokemon_select as pokemon_select
import includes.winner as win
from includes.fight_start import FightStart

pg.init()

imagesPath = "resources/images/"

screen = pg.display.set_mode((640, 495))
Game = Fight(screen)

icon = pg.image.load("resources/images/pokeball.ico")
background = pg.image.load("resources/images/fight_area.jpg")

pg.display.set_caption("Pokémon")
pg.display.set_icon(icon)

isRunning = True

while isRunning:
    screen.blit(background, (0, 0))

    if Game.FightIsEnd:
        win.Winner(screen, Game.Winner)
    elif Game.IsPlaying:
        if Game.IsSelected:
            FightStart(screen, Game)
        else:
            pokemon_select.DisplayPokemonsList(screen, Game.PokemonsGroup)
    else:
        main_menu.SetDisplay(screen, background)

    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
            pg.quit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if Game.FightIsEnd and win.buttonMainMenuRect.collidepoint(event.pos):
                Game.Winner = ""
                Game.FightIsEnd = False
                print("OK")
            elif not Game.IsPlaying and main_menu.buttonPlayRect.collidepoint(event.pos):
                Game.IsPlaying = True
            else:
                for pokemon in Game.PokemonsGroup:
                    if pokemon["rect"].collidepoint(event.pos):
                        Game.SetFighters(Game.pokedex.GetPokemonByName(pokemon["name"]))
                        Game.IsSelected = True
                        break
