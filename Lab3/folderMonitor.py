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