import os
import time
from datetime import datetime
from allFiles import AllFiles
from textFiles import TextFiles
from programFiles import ProgramFiles
from imageFiles import ImageFiles

class FolderMonitor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.snapshot_time = time.time()
        self.file_info = []


    def commit(self):
        self.snapshot_time = time.time()
        snapshotTime = datetime.fromtimestamp(self.snapshot_time)
        print("Snapshot time updated!", snapshotTime)
    
    def info(self,name):
        for file in os.listdir(self.folder_path):
            if file == name:
                file_path = self.folder_path + "\\" + name
                extension = os.path.splitext(file)[1]
                created = datetime.fromtimestamp(os.path.getctime(file_path))
                updated = datetime.fromtimestamp(os.path.getmtime(file_path))
                if ".txt" in name:
                    textFiles = TextFiles(None, None, None, None, None, None, None)
                    lineCount = textFiles.number_of_lines(file_path)
                    wordCount = textFiles.number_of_words(file_path)
                    characterCount = textFiles.number_of_charaters(file_path)
                    textFilesObject = TextFiles(file,extension,created,updated,lineCount,wordCount,characterCount)
                    print(f"Name: {textFilesObject.name}\n"
                            f"Extension: {textFilesObject.extenstion}\n"
                            f"Created: {textFilesObject.created}\n"
                            f"Updated: {textFilesObject.updated}\n"
                            f"Line Count: {textFilesObject.lineCount}\n"
                            f"Word Count: {textFilesObject.wordCount}\n"
                            f"Character Count: {textFilesObject.characterCount}")
                if (".png" in name) or (".jpg" in name):
                    imageFiles = ImageFiles(None, None, None, None, None)
                    imageSize = imageFiles.get_size(file_path)
                    imageFilesObject = ImageFiles(file,extension,created,updated,imageSize)
                    print(f"Name: {imageFilesObject.name}\n"
                            f"Extension: {imageFilesObject.extenstion}\n"
                            f"Created: {imageFilesObject.created}\n"
                            f"Updated: {imageFilesObject.updated}\n"
                            f"Image Size: {imageFilesObject.imageSize}")
                if (".java" in name) or (".py" in name):
                    programFiles = ProgramFiles(None, None, None, None, None, None, None)
                    lineCount = programFiles.number_of_lines(file_path)
                    classCount = programFiles.number_of_clases(file_path)
                    methodCount = programFiles.number_of_methodes(file_path)
                    programFilesObject = ProgramFiles(file,extension,created,updated,lineCount,classCount,methodCount)
                    print(f"Name: {programFilesObject.name}\n"
                    f"Extension: {programFilesObject.extenstion}\n"
                    f"Created: {programFilesObject.created}\n"
                    f"Updated: {programFilesObject.updated}\n"
                    f"Line Count: {programFilesObject.lineCount}\n"
                    f"Class Count: {programFilesObject.classCount}\n"
                    f"Method Count: {programFilesObject.methodCount}")
                    
    def scan(self):
        for file in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file)
            if os.path.isfile(file_path):
                updated = datetime.fromtimestamp(os.path.getmtime(file_path))
                file_data = {'file_name': file, 'updated_date': updated}
                self.file_info.append(file_data)
        return self.file_info
    
    def snapshotTime(self):
        self.snapshot_time = time.time()
        return self.snapshot_time
    
    def status(self,past):
        for file in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file)
            if os.path.isfile(file_path):
                updated = datetime.fromtimestamp(os.path.getmtime(file_path))
                file_data = {'file_name': file, 'updated_date': updated}
                self.file_info.append(file_data)
        for presentElements in self.file_info:
            for pastElements in past:
                if presentElements.file_name == pastElements.file_name and presentElements.datetime == pastElements.datetime:
                    print(presentElements.file_nam," - ","No Changes")
                if presentElements.file_name == pastElements.file_name and presentElements.datetime != pastElements.datetime:
                    print(presentElements.file_nam," - ","Changed")
                if presentElements.file_name != pastElements.file_name and presentElements.datetime == pastElements.datetime:
                    print(presentElements.file_nam," - ","New File")
        for pastElements in past:
            for presentElements in self.file_info:
                if presentElements.file_name != pastElements.file_name and presentElements.datetime == pastElements.datetime:
                    print(presentElements.file_nam," - ","Deleted")
    