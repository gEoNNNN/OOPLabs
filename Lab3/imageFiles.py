import datetime
import os
from allFiles import File
from PIL import Image

class ImageFiles(File):
    def __init__(self, name, extension, created, updated, imageSize):
        super().__init__(name, extension, created, updated)
        self.imageSize = imageSize
    
    def get_size(self,file_path):
        image = Image.open(file_path)
        width, height = image.size
        size = str(width) + "x" + str(height)
        return size
    
    def programInfo(self, folder_path, name):
        for file in os.listdir(folder_path):
            if file == name:
                file_path = os.path.join(folder_path, name)
                extension = os.path.splitext(file)[1]
                created = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
                updated = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                self.imageSize = self.get_size(file_path)
                print(f"Name: {name}\n"
                            f"Extension: {extension}\n"
                            f"Created: {created}\n"
                            f"Updated: {updated}\n"
                            f"Image Size: {self.imageSize}")