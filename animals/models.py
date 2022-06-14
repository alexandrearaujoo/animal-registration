from operator import mod
import re
from django.db import models

# Create your models here.
class Animal (models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15)

    groups = models.ForeignKey('groups.Group', on_delete=models.CASCADE, related_name='groups')
    characteriscs = models.ManyToManyField(
        'characteristcs.Characteristc', 
        on_delete=models.CASCADE, 
        related_name='characteristcs'
    ) 