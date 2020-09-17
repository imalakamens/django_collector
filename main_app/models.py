from django.db import models
from django.urls import reverse

RATINGS = (
    ('1', 'Not so good...'),
    ('2', 'Could be better'),
    ('3', 'It was alright'),
    ('4', 'Pretty good...'),
    ('5', 'AMAZING!')
)

# Create your models here.
class Record(models.Model):
    album_title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    year = models.IntegerField()
    size = models.IntegerField()

    def __str__(self):
        return self.album_title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'record_id' : self.id})

class Review(models.Model):
    description = models.TextField(max_length=250)
    rating = models.CharField(
        max_length=1,
        choices=RATINGS,
        default=RATINGS[2][0]
        )

    record=models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_rating_display()}'