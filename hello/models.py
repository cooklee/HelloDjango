from django.db import models

# Create your models here.




class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    #book_set UWAGA !!!!  To pole jest magiczne bo tworzy sie samo magia DJANGO


genre_choises = (
    (1, 'Kryminał'),
    (2, 'Horror'),
    (3, 'Fantasy'),
    (4, 'Romans'),
)
class Book(models.Model):
    title = models.CharField(max_length=123)
    year = models.IntegerField()
    genre = models.IntegerField(choices=genre_choises, default=1)
    author = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, )



