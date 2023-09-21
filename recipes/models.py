from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    img = models.CharField()
    url = models.CharField()
    author = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
