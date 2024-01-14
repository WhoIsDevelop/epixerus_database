
from epixerus_database.db_libs.lib_abc import AbstractBD

class LibSQLite3(AbstractBD):
    def __init__(self, name):
        super().__init__()
        self.name = name


