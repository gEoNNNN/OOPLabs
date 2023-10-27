from allFiles import AllFiles
from PIL import Image

class ImageFiles(AllFiles):
    def __init__(self, name, extension, created, updated, imageSize):
        super().__init__(name, extension, created, updated)
        self.imageSize = imageSize
    
    def get_size(self,file_path):
        image = Image.open(file_path)
        width, height = image.size
        size = str(width) + "x" + str(height)
        return size