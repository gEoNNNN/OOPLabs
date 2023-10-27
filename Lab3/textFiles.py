from allFiles import AllFiles

class TextFiles(AllFiles):
    def __init__(self, name, extension, created, updated, lineCount, wordCount, characterCount):
        super().__init__(name, extension, created, updated)
        self.lineCount = lineCount
        self.wordCount = wordCount
        self.characterCount = characterCount

    def number_of_lines(self,file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
        return line_count
    
    def number_of_words(self,file_path):
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split()
        word_count = len(words)
        return word_count
    
    def number_of_charaters(self,file_path):
        with open(file_path, "r") as file:
            content = file.read()
            character_count = len(content)
        return character_count