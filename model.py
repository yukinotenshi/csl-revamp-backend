import peewee as pw
from playhouse.shortcuts import model_to_dict


db = pw.SqliteDatabase('data.db')


class Scholar(pw.Model):
    name = pw.CharField()
    university = pw.CharField()
    description = pw.TextField()
    image = pw.CharField()
    cv = pw.CharField(null=True)
    linkedin = pw.CharField(null=True)

    def to_dict(self):
        return model_to_dict(self)

    class Meta:
        database = db
