from abc import ABC, abstractmethod

class AbstractBD(ABC):
    def __init__(self):
        self._connection = None
        self._name = None
        self._address = None

    @abstractmethod
    def table(self, table_name):
        return AbstractTable(self,table_name)

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
    def create(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def clear(self):
        pass

class AbstractTable(ABC):

    def __init__(self,parent, table_name):
        self.table_name = table_name
        self.parent=parent

    @abstractmethod
    def check(self):
        pass

    @abstractmethod
    def create(self, table_dictionary):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def custom(self):
        pass


class AbstractView(ABC):

    def __init__(self,parent, view_name):
        self.view_name = view_name
        self.parent = parent

    @abstractmethod
    def check(self):
        pass


    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def select(self):
        pass