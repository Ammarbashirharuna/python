from abc import ABC, abstractmethod
class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def open(self):
        self.open = False
    
    def open(self):
        if self.opened:
            raise InvalidOperationError("stream is already open")
        self.open = True
    def close(self):
        if not self.opened:
            raise InvalidOperationError("stream is already close")
        self.open = False

    @abstractmethod
    def read(self):
        pass



class FileStream(Stream):
    def read(self):
        print("reading data from a file")


class NerworkStream(Stream):
    def read(self):
        print("reading data from a file")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from a file")