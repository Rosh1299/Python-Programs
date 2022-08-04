from abc import ABC, abstractmethod

# custom exception


class InvalidOperationError(Exception):
    pass

# implementation of inheritance


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("stream is already open.")
        self.opened == True

    def open(self):
        if not self.opened:
            raise InvalidOperationError("stream is already open.")
        self.opened == False

    # implementation of data abstraction
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from memory stream")


stream = Stream()
# stream1 = MemoryStream()
# it will give error as we cant't instantiate object of abstract class.
print(stream.read())
