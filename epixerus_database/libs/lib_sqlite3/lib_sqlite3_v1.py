import sqlite3

from epixerus_database.libs.lib_abc import AbstractBD

class LibSQLite3(AbstractBD):


    def __init__(self):
        super().__init__()
        self._file_extension = '.db'

    @property
    def database_path(self):
        return self._address + self._name + self._file_extension

    def close(self):
        if self._connection:
            self._connection.close()
            self._connection = None

    def connect(self):
        self._connection = sqlite3.connect(self.database_path)

    def config(self, **kwargs):
        if 'file_extension' in kwargs:
            self._file_extension = kwargs.get('file_extension')
        if 'name' in kwargs:
            self._name = kwargs.get('name')
        if 'address' in kwargs:
            self._address = kwargs.get('address')
    def check(self, name=None):
        pass

    def database_create(self):
        pass

    def database_delete(self):
        pass

    def table_create(self, table_name):
        pass

    def table_delete(self, table_name):
        pass

    def table_select(self, table_name):
        pass

    def table_insert(self, table_name):
        pass