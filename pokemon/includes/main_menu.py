import pygame as pg

banner = pg.image.load("resources/images/banner.png")
buttonPlay = pg.image.load("resources/images/buttons/play.png")
buttonPlayRect = buttonPlay.get_rect()


def SetDisplay(screen, background):
    buttonPlayRect.x = background.get_width() / 2 - banner.get_width() / 2 - 20
    buttonPlayRect.y = banner.get_height() + 68

    screen.blit(banner, (background.get_width() / 2 - banner.get_width() / 2, 20))
    screen.blit(buttonPlay, buttonPlayRect)
