from allFiles import AllFiles

class TextFiles(AllFiles):
    def __init__(self, name, extension, created, updated, lineCount, wordCount, characterCount):
        super().__init__(name, extension, created, updated)
        self.lineCount = lineCount
        self.wordCount = wordCount
        self.characterCount = characterCount