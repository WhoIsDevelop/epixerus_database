
from epixerus_database.libs.lib_abc import AbstractBD

class LibSQLite3(AbstractBD):

    def __init__(self):
        super().__init__()
        self.name = None

    def close(self):
        pass

    def connect(self):
        pass



    def config(self, name, path=None, **kwargs):
        pass
