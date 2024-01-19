
from epixerus_database import EpixerusDataBase

db = EpixerusDataBase(EpixerusDataBase.LIBS.SQLite3)
db.lib.config(name='a')

with db:
    db.lib.table_create(table_name='test')
    db.lib.table_insert(table_name='test')

x = 12