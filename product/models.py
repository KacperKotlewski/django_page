from django.db import models
from track.models import Track

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)

    track_ch = "album"
    PRODUCT_TYPES = [
        (track_ch, 'album'),
    ]
    product_type = models.CharField(
        choices=PRODUCT_TYPES,
        default=track_ch,
        max_length=64,
    )
    
    price = models.FloatField(blank=True, null=True)
    unlimited = models.BooleanField(default=False)
    count = models.IntegerField(blank=True, null=True)

    
    track = models.ForeignKey(Track, on_delete=models.CASCADE, blank=True, null=True)

    def get_link(self):
        if self.product_type == "album":
            return self.track.friendly_link