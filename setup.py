from model import *


db.connect()
db.create_tables([Scholar, ScholarApp, SponsorApp, Board])
db.close()
