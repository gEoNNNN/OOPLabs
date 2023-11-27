import datetime
import os
from allFiles import File

class TextFiles(File):
    def __init__(self, name, extension, created, updated, lineCount, wordCount, characterCount):
        super().__init__(name, extension, created, updated)
        self.lineCount = lineCount
        self.wordCount = wordCount
        self.characterCount = characterCount

    def number_of_lines(self, file_path):
        with open(file_path, 'r') as f:
            return sum(1 for line in f)
    
    def number_of_words(self, file_path):
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split()
        word_count = len(words)
        return word_count
    
    def number_of_characters(self, file_path):
        with open(file_path, "r") as file:
            content = file.read()
            character_count = len(content)
        return character_count
    
    def programInfo(self, folder_path, name):
        for file in os.listdir(folder_path):
            if file == name:
                file_path = os.path.join(folder_path, name)
                extension = os.path.splitext(file)[1]
                created = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
                updated = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                self.lineCount = self.number_of_lines(file_path)
                self.wordCount = self.number_of_words(file_path)
                self.characterCount = self.number_of_characters(file_path)
                print(f"Name: {name}\n"
                      f"Extension: {extension}\n"
                      f"Created: {created}\n"
                      f"Updated: {updated}\n"
                      f"Line Count: {self.lineCount}\n"
                      f"Word Count: {self.wordCount}\n"
                      f"Character Count: {self.characterCount}")
