from allFiles import AllFiles

class TextFiles(AllFiles):
    def __init__(self, name, extension, created, updated, lineCount, wordCount, characterCount):
        super().__init__(name, extension, created, updated)
        self.lineCount = lineCount
        self.wordCount = wordCount
        self.characterCount = characterCount

    def number_of_lines(self,file_path):
        with open(file_path, 'r') as f:
            return sum(1 for line in f)
    
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
    
    def txtInfo(self,file_path):
        lineCount = self.number_of_lines(file_path)
        wordCount = self.number_of_words(file_path)
        characterCount = self.number_of_charaters(file_path)
        textFilesObject = TextFiles(self.name,self.extension,self.created,self.updated,self.lineCount,self.wordCount,self.characterCount)
        print(f"Name: {textFilesObject.name}\n"
                f"Extension: {textFilesObject.extenstion}\n"
                f"Created: {textFilesObject.created}\n"
                f"Updated: {textFilesObject.updated}\n"
                f"Line Count: {textFilesObject.lineCount}\n"
                f"Word Count: {textFilesObject.wordCount}\n"
                f"Character Count: {textFilesObject.characterCount}")