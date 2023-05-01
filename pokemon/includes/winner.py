import pygame as pg

buttonMainMenu = pg.image.load("resources/images/buttons/menu_button.png")
buttonMainMenuRect = buttonMainMenu.get_rect()
buttonMainMenuRect.x = 220
buttonMainMenuRect.y = 250


def Winner(screen, winner):
    font = pg.font.SysFont("Trebuchet MS", 36, True)

    if len(winner) == 0:
        text = font.render("Match nul !", True, (0, 0, 0))
        screen.blit(text, (230, 180))
    else:
        text = font.render(f"{winner.capitalize()} remporte le combat !", True, (0, 0, 0))
        screen.blit(text, (70, 180))

    screen.blit(buttonMainMenu, buttonMainMenuRect)
