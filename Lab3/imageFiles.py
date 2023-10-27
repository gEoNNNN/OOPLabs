from allFiles import AllFiles
from PIL import Image

class ImageFiles(AllFiles):
    def __init__(self, name, extension, created, updated, imageSize):
        super().__init__(name, extension, created, updated)
        self.imageSize = imageSize