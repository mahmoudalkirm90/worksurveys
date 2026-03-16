from handle_DB import DB

db = DB('codes.db')
db.create_table('admins(username varchar(20), password varchar(20))')
db.cursor.execute('insert into admins(username,password) values(?,?)' , ('mahmoudalkirm' , 'mahmoud123'))
db.commit()

