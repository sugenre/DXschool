from django.db import models

class Item(models.Model):
    itemid = models.CharField(max_length=50, primary_key=True)
    itemname = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    pictureurl = models.CharField(max_length=100)
# Create your models here.
