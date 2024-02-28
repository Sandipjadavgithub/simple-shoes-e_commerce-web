from django.db import models

class Shoes(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    quantity= models.IntegerField()
    image =models.CharField(max_length=2083)
