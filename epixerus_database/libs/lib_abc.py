from abc import ABC, abstractmethod

class AbstractBD(ABC):
    def __init__(self):
        self._connection = None
        self._name = None
        self._address = None

    @abstractmethod
    def config(self, name=None, address=None, user=None, password=None, file_extension=None, **kwargs):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def check(self):
        pass

    @abstractmethod
    def database_create(self):
        pass

    @abstractmethod
    def database_delete(self):
        pass

    @abstractmethod
    def table_create(self, table_name):
        pass

    @abstractmethod
    def table_delete(self, table_name):
        pass

    @abstractmethod
    def table_select(self, table_name):
        pass

    @abstractmethod
    def table_insert(self, table_name):
        pass
