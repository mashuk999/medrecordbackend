from django.db import models

# Create your models here.
class medicines(models.Model):
    name = models.TextField()
    mrp = models.FloatField()
    rate = models.FloatField()
    pr = models.FloatField()