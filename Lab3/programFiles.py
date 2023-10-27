from allFiles import AllFiles
import re

class ProgramFiles(AllFiles):
    def __init__(self, name, extension, created, updated, lineCount, classCount, methodCount):
            super().__init__(name, extension, created, updated)
            self.lineCount = lineCount
            self.classCount = classCount
            self.methodCount = methodCount

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
