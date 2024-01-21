
from epixerus_database import EpixerusDataBase

db = EpixerusDataBase(EpixerusDataBase.LIBS.SQLite3)
db.lib.config(name='a')

with db:
    db.lib.table('_').create()
    db.lib.table('x').delete()

x = 12