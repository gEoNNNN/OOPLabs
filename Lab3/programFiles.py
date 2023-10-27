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
        with open(file_path, 'r') as file:
            content = file.read()
            class_pattern = re.compile(r'class\s+\w+\s*[{(]')
            classes = class_pattern.findall(content)
            class_count = len(classes)
        return class_count
        
    def number_of_methodes(self,file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            method_pattern = re.compile(r'def\s+\w+\s*\([^)]*\)\s*[{(]')
            methods = method_pattern.findall(content)
            method_count = len(methods)
        return method_count     
