from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

class Book(models.Model):
    title = models.CharField(max_length=123)
    year = models.IntegerField()


