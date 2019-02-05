from model import *


db.connect()
db.create_tables([Scholar, ScholarApp, SponsorApp])
db.close()
