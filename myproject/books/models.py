from django.db import models

class Collection(models.Model):
    book_name = models.CharField(max_length=100)
    discription = models.CharField(max_length=500)  
    bookcover = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.book_name


class Piece(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    year = models.IntegerField()
    piececover = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

# Create your models here.
