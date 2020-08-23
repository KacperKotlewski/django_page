from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Track(models.Model):
    title = models.CharField(max_length=100)
    friendly_link = models.SlugField(unique=True, max_length=60, blank=True)
    image = models.ImageField(upload_to="image", blank=True, null=True)
    bg_image = models.ImageField(upload_to="image", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

        #Then override models save method:
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Track, self).save(*args, **kwargs)

    def __str__(self):
        return self.title