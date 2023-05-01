import pygame as pg


def DisplayPokemonsList(screen, pokemons):
    font = pg.font.SysFont("Trebuchet MS", 32, True)
    text = font.render("Sélectionne ton pokémon", True, (0, 0, 0))
    screen.blit(text, (120, 120))

    for pokemon in pokemons:
        screen.blit(pokemon["img"], pokemon["rect"])
