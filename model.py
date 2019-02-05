import peewee as pw
from datetime import datetime
from playhouse.shortcuts import model_to_dict


db = pw.SqliteDatabase('data.db')


class BaseModel(pw.Model):
    created_at = pw.DateTimeField(default=datetime.now)

    def to_dict(self):
        return model_to_dict(self)

    class Meta:
        database = db


class Scholar(BaseModel):
    name = pw.CharField()
    university = pw.CharField()
    description = pw.TextField()
    image = pw.CharField()
    cv = pw.CharField(null=True)
    linkedin = pw.CharField(null=True)


class ScholarApp(BaseModel):
    name = pw.CharField()
    email = pw.CharField()
    address = pw.CharField()
    university = pw.CharField()


class SponsorApp(BaseModel):
    name = pw.CharField()
    email = pw.CharField()
    position = pw.CharField()
    company = pw.CharField()
    phone = pw.CharField()
