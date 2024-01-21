from epixerus_database.libs import LibSQLite3, AbstractBD
from enum import Enum

class EpixerusDataBase:

    class LIBS(Enum):
        SQLite3 = LibSQLite3


    def __init__(self, lib):
        self.lib: AbstractBD = lib.value()

    def __enter__(self):
        self.lib.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.lib.close()

    def __getattr__(self, attr):
        return getattr(self.lib, attr)
