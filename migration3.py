from handle_DB import DB
db = DB('codes.db')
added = db.add_codes('life points',n=100)

print(added)