from django.db import models
from track.models import Track

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=100)
    friendly_link = models.SlugField(max_length=60, blank=True)
    id_in_track = models.IntegerField(blank=True, null=True)
    audio = models.FileField(upload_to="audio", blank=True, null=True)
    image = models.ImageField(upload_to="image", blank=True, null=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        try:
            return '"' + self.title + '" z albumu "' + self.track.title + '"'
        except:
            return '"' + self.title + '"'
