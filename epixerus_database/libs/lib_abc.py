from abc import ABC, abstractmethod

class AbstractBD(ABC):
    def __init__(self):
        self.connection = None

    @abstractmethod
    def config(self, name, path=None, user=None, password=None, address=None, **kwargs):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    #
    # @abstractmethod
    # def do_another_thing(self):
    #     pass