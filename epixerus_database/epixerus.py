from epixerus_database.db_libs import LibSQLite3
from enum import Enum

class EpixerusDataBase:

    class LibSelector(Enum):
        SQLite3 = 1

    Libs = {
        LibSelector.SQLite3: LibSQLite3,
    }

    def __init__(self, lib, name):
        self.lib = self.Libs.get(lib)(name)



