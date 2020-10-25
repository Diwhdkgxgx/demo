from django.db import models
from firstweek.settings import *
# Create your models here.
class Student(models.Model):
    name = models.CharField(u'姓名', max_length=10, default='ccq')
    age = models.IntegerField(u'年龄')
    grade = models.FloatField(u'成绩', default=60)
    description = models.TextField(u'简介',max_length=100)
    choice = (
        (0,"男"),
        (1,"女")
    )
    sex = models.IntegerField( u'性别', choices=choice)
#session