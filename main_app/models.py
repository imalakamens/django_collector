from django.db import models

# Create your models here.
class Record(models.Model):
    album_title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    year = models.IntegerField()
    size = models.IntegerField()

    def __str__(self):
        return self.album_title