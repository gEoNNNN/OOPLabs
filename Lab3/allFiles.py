import datetime
import os


class AllFiles:
    def __init__(self, name, extension, created, updated):
        self.name = name
        self.extension = extension
        self.created = created
        self.updated = updated

    def from_file_path(cls, folder_path, file_name):
        file_path = os.path.join(folder_path, file_name)
        extension = os.path.splitext(file_name)[1]
        created = datetime.fromtimestamp(os.path.getctime(file_path))
        updated = datetime.fromtimestamp(os.path.getmtime(file_path))
        return cls(file_name, extension, created, updated)
