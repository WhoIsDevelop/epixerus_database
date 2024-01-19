
from epixerus_database import EpixerusDataBase

db = EpixerusDataBase(EpixerusDataBase.LIBS.SQLite3)
db.lib.config(name='a')
with db:
    x = db.lib.table_create('text')
