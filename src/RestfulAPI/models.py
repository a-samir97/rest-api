from django.db import models

# Create your models here.

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    budget = models.IntegerField()
    goal = models.CharField(max_length=60)
    category = models.CharField(max_length=60)


