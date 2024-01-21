import sqlite3
import os

from epixerus_database.libs.lib_abc import AbstractBD, AbstractTable

class LibSQLite3V1(AbstractBD):


    def table(self, table_name):
        return TableSQLite3(self,table_name)

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

    def check(self):
        cursor = self.parent._connection.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table_name}'")
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False

    def custom(self):
        pass

    def clear(self):
        pass

    def create(self, table_params):
        cursor = self.parent._connection.cursor()

        create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {self.table_name} {table_params}
        '''
        cursor.execute(create_table_query)

        self.parent._connection.commit()

    def delete(self):
        pass

    def select(self):
        pass

    def insert(self, values):
        values = (None, *values)
        cursor = self.parent._connection.cursor()
        insert_query = f"INSERT INTO {self.table_name} VALUES ({', '.join(['?' for _ in values])})"

        cursor.execute(insert_query, values)
        self.parent._connection.commit()

    def __init__(self, parent, table_name):
        super().__init__(parent, table_name)
