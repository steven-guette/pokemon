"""
@Author  : GUETTE Steven
@Class   : JSONFile
@Version : 1.0.1
@Since   : 2023
"""

import json
from classes.whiteshield import WShield
from classes.file import File


class JSONFile(File):
    def __int__(self, relpath, writeAppend):
        File.__init__(self, relpath, writeAppend)

    # region GETTERS

    def GetContent(self, byLoadMethod=False):
        fileContent = list()

        if self.FileExists(self.Filepath):
            with open(self.Filepath, "r") as file:
                if byLoadMethod:
                    fileContent = json.load(file)
                else:
                    for fileLine in file:
                        fileContent.append(json.loads(fileLine))

        return fileContent

    # endregion

    # Region SETTERS

    def SetContent(self, datas, byDumpMethod=False):
        toAdd = list()

        if WShield.IsString(datas):
            toAdd.append(datas)
        elif WShield.IsList(datas):
            toAdd.extend(datas)
        elif WShield.IsDict(datas):
            toAdd = datas

        if len(toAdd) > 0:
            self.CreateDir(self.Filepath)

            mode = "w"
            if self.WriteAppend and not byDumpMethod:
                mode = "a"

            with open(self.Filepath, mode) as file:
                if byDumpMethod:
                    json.dump(toAdd, file)
                else:
                    for newLine in toAdd:
                        file.write("{}\n".format(json.dumps(newLine)))

            return True
        return False

    # endregion
