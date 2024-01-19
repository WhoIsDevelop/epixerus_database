
from epixerus_database import EpixerusDataBase

db = EpixerusDataBase(EpixerusDataBase.LIBS.SQLite3)
db.lib.config(name='a')
x = 2