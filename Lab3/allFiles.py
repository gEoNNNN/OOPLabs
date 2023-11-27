import datetime
import os
from abc import abstractmethod


class File:
    def __init__(self, name, extension, created, updated):
        self.name = name
        self.extension = extension
        self.created = created
        self.updated = updated

    @abstractmethod
    def programInfo():
        pass
