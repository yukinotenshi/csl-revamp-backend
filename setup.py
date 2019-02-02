from model import db, Scholar


db.connect()
db.create_tables([Scholar])
db.close()
