from handle_DB import DB

db  = DB('codes.db')
db.create_table('registerations(code varchar(8),email varchar(256), first_name varChar(20) ,last_name varChar(20), state varchar(20))')
db.commit()