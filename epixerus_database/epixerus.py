from epixerus_database.libs import LibSQLite3, AbstractBD
from enum import Enum

class EpixerusDataBase:

    class LIBS(Enum):
        SQLite3 = LibSQLite3


    def __init__(self, lib):
        self.lib: AbstractBD = lib.value()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def connect(self):
        self.lib.connect()

    def close(self):
        if self.lib.connection:
            self.lib.connection.close()

    def check(self, name=None):
        pass

    def database_create(self):
        pass

    def database_delete(self):
        pass

    def table_create(self, name=None):
        pass

    def table_delete(self, name=None):
        pass

    def table_select(self, name=None):
        pass

    def table_insert(self):
        pass