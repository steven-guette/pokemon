import pygame as pg


class CommentBox(pg.sprite.Sprite):
    def __init__(self, pokemon, comment):
        super().__init__()

        self.pokemon = pokemon
        self.velocity = 1
        self.textAlpha = 255
        self.font = pg.font.SysFont("Comic Sans MS", 18, True)
        self.text = self.font.render(comment, True, (0, 0, 0))
        self.textRect = self.text.get_rect()

        self.SetComment(comment)

    def MoveUp(self):
        self.textRect.y -= self.velocity
        self.SetTextAlpha()

    def SetTextAlpha(self):
        self.text.set_alpha(self.textAlpha)
        self.textAlpha -= 2

    def SetComment(self, comment):
        if comment != "Esquive !":
            textColor = (255, 99, 71)

            if comment == "-":
                textPosition = (self.pokemon.rect.x + 5, self.pokemon.rect.y - 50)
            else:
                textPosition = (self.pokemon.rect.x - 15, self.pokemon.rect.y - 50)
        else:
            textColor = (0, 0, 0)
            textPosition = (self.pokemon.rect.x - 5, self.pokemon.rect.y - 50)

        self.text = self.font.render(comment, True, textColor)

        self.textRect = self.text.get_rect()
        self.textRect.x = textPosition[0]
        self.textRect.y = textPosition[1]
