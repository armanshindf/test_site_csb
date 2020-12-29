from django.db import models

# Create your models here.


class Categories(models.Model):
    parent_id = models.IntegerField
    name = models.CharField


class Stuff(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField
    cost = models.FloatField
