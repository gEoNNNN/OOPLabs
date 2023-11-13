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
                    textFiles.txtInfo(name)
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
        snapshotTime = datetime.fromtimestamp(self.snapshot_time)
        return snapshotTime

    def scan(self):
            file_info_temp = []
            for file in os.listdir(self.folder_path):
                file_path = os.path.join(self.folder_path, file)
                if os.path.isfile(file_path):
                    updated = datetime.fromtimestamp(os.path.getmtime(file_path))
                    file_data = {'file_name': file, 'updated_date': updated}
                    file_info_temp.append(file_data)
            return file_info_temp
    
    def snapshotTime(self):
        return datetime.fromtimestamp(self.snapshot_time)

    def display_options(self):
        print("\nOptions:")
        print("1. commit")
        print("2. info <filename>")
        print("3. status")
        print("4. exit")
    
    def status(self, past,current):
        processed_files = set()
        for presentElement in current:
            found = False
            for pastElement in past:
                if presentElement['file_name'] == pastElement['file_name']:
                    found = True
                    processed_files.add(pastElement['file_name'])
                    if presentElement['updated_date'] != pastElement['updated_date']:
                        print(presentElement['file_name'], " - ", "Changed")
                    elif presentElement['updated_date'] == pastElement['updated_date']:
                        print(presentElement['file_name'], " - ", "No Changes")
                    break
            if not found:
                print(presentElement['file_name'], " - ", "New File")

        for pastElement in past:
            if pastElement['file_name'] not in processed_files:
                print(pastElement['file_name'], " - ", "Deleted")

    def Schedule(self,past,current):
            processed_files = set()
            for presentElement in current:
                found = False
                for pastElement in past:
                    if presentElement['file_name'] == pastElement['file_name']:
                        found = True
                        processed_files.add(pastElement['file_name'])
                        if presentElement['updated_date'] != pastElement['updated_date']:
                            print("\n" + presentElement['file_name'], " - ", "Changes")
                        break
                if not found:
                    print("\n" + presentElement['file_name'], " - ", "New File")

            for pastElement in past:
                if pastElement['file_name'] not in processed_files:
                    print("\n" + pastElement['file_name'], " - ", "Deleted")


            