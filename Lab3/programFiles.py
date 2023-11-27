import datetime
import os
from allFiles import File
import re

class ProgramFiles(File):
    def __init__(self, name, extension, created, updated, lineCount, classCount, methodCount):
        super().__init__(name, extension, created, updated)
        self.lineCount = lineCount
        self.classCount = classCount
        self.method_count = methodCount

    def number_of_lines(self,file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
        return line_count
    
    def number_of_clases(self,file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        if file_path.endswith('.py'):
            return content.count('class ')
        elif file_path.endswith('.java'):
            return sum(content.count(keyword) for keyword in [' class ', ' interface ', ' enum ', ' @interface '])
        else:
            return 0
        
    def number_of_methodes(self,file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        if file_path.endswith('.py'):
            return sum(1 for line in lines if line.strip().startswith('def '))

        elif file_path.endswith('.java'):
            return sum(1 for line in lines if '(' in line and ')' in line and '{' in line)

        else:
            return 0   
        
    def programInfo(self, folder_path, name):
        for file in os.listdir(folder_path):
            if file == name:
                file_path = os.path.join(folder_path, name)
                extension = os.path.splitext(file)[1]
                created = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
                updated = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                self.lineCount = self.number_of_lines(file_path)
                self.classCount = self.number_of_clases(file_path)
                self.method_count = self.number_of_methodes(file_path)
                print(f"Name: {name}\n"
                    f"Extension: {extension}\n"
                    f"Created: {created}\n"
                    f"Updated: {updated}\n"
                    f"Line Count: {self.lineCount}\n"
                    f"Class Count: {self.classCount}\n"
                    f"Method Count: {self.method_count}")
