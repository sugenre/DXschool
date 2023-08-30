from django.db import models

class ToDo(models.Model):
    id = models.AutoField(primary_key = True) #auto_increment
    userid = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    done = models.BooleanField()
    regdate = models.DateTimeField(auto_now_add =True)
    moddate = models.DateTimeField(null=True)

# Create your models here.
