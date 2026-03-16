import sqlite3
import string
from random import choice
class DB:
    def __init__(self,dbname:str):
        try:
            self.db = sqlite3.connect(dbname , check_same_thread=False
                                       )
            self.cursor = self.db.cursor()

        except sqlite3.Error:
            print(sqlite3.Error)
    def create_table(self,table:str):
        self.cursor.execute(f'create table if not exists {table}')
        self.db.commit()
    def add_codes(self,site:str,n:int):
        added = []
        characters = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for i in range(0,n):
            code = ''
            for j in range(0,8):
                code += choice(characters)
            self.cursor.execute('insert into codes(site,code) values(?,?)' , (site,code))
            added.append(code)
            self.db.commit()
        return added
    def check_code(self, code):
     self.cursor.execute('select * from codes')
     data = self.cursor.fetchall()
     for i in data:
         if i[0] == code and i[2] == 1:
             return i[1]
     return False
    def disable_code(self,code):
        self.cursor.execute(f'''update codes
                               set is_active = 0
                               where code = ?
                            ''', (code,))
        self.db.commit()
    def commit(self):
        self.db.commit()
    def check_admin(self,username,password):
        self.cursor.execute('select * from admins')
        data = self.cursor.fetchall()
        for i in data:
            if i[0] == username and i[1] == password:
                return True
        return False
    def regist(self,code,email,first_name,last_name,state):
        self.cursor.execute('insert into registerations(code,email, first_name,last_name, state) values(?,?,?,?,?)'
                            , (code,email,first_name,last_name,state))
        self.db.commit()
    def get_registerations(self,n):
        # reutrn email, code, state
        self.cursor.execute(f'select code,email,state from registerations limit {n}')
        data = []
        for i in self.cursor.fetchall():
            ob = {
                'code':i[0],
                'email':i[1],
                'state':i[2]
            }
            data.append(ob)
        return data
    def get_codeSite(self,code):
        self.cursor.execute(f"select site from codes where code = ?" ,
                            (code,))
        return self.cursor.fetchone()[0]
# db = DB('codes.db')
# print(db.get_codeSite('QCv3d6AE'))