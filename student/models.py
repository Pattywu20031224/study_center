from django.db.models import *

# Create your models here.
class student(Model):
    name = CharField('姓名', max_length=32)
    idnumber = CharField('學號', max_length=255)
    email = EmailField('電子信箱')
    classroom = CharField('班級', max_length=3)
    number = CharField('座號', max_length=2)
    def __str__(self):
        return "{} / {} / {}".format(
            self.name,
            self.classroom, 
            self.number, 
        )