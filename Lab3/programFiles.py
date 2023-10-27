from allFiles import AllFiles
import re

class ProgramFiles(AllFiles):
    def __init__(self, name, extension, created, updated, lineCount, classCount, methodCount):
            super().__init__(name, extension, created, updated)
            self.lineCount = lineCount
            self.classCount = classCount
            self.methodCount = methodCount