import sqlite3
import os

from epixerus_database.libs.lib_abc import AbstractBD, AbstractTable

class LibSQLite3V1(AbstractBD):


    def table(self, table_name):
        return TableSQLite3(table_name)

    def clear(self):
        pass

    def __init__(self):
        super().__init__()
        self._address = os.path.dirname(os.path.abspath(__file__)) + '/'
        self._name = 'default'
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

    def check(self):
        self.connect()
        self.close()

    def create(self):
        pass

    def delete(self):
        pass


class TableSQLite3(AbstractTable):

    def custom(self):
        pass

    def clear(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def select(self):
        pass

    def insert(self):
        pass

    def __init__(self, table_name):
        super().__init__(table_name)
