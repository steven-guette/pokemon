from classes.jsonfile import JSONFile


class Pokedex(JSONFile):
    def __init__(self):
        super().__init__("resources/datas/pokedex.json", True)
        self.__pokedexList = self.GetContent()

    # region GETTERS ####################

    def GetPokemonsList(self):
        return self.__pokedexList

    def GetPokemonByName(self, pokemonName):
        for pokemon in self.__pokedexList:
            if pokemon["name"] == pokemonName:
                return pokemon

    def GetPokemonByID(self, index):
        if 0 <= index < len(self.__pokedexList):
            return self.__pokedexList[index]

        return False

    # endregion #########################
