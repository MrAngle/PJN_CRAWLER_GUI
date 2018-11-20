class Article:


    def __init__(self, directoryName):
        self.directoryName = directoryName

    def getDirectoryName(self):
        return self.directoryName
    
    def getTextFromArtile(self, pathToFile):
        try:
            filePath = pathToFile + self.directoryName + "\\correctWords.txt"
            f = open(filePath, "r")
            str = f.read()
            f.close()
        except:
            print("Something wrong with file - ARTICLE")
            return " "
        return str
        