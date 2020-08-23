from django.db import models

# Create your models here.

class ExternalLink(models.Model):
    page_name = models.CharField(max_length=128)
    link = models.TextField(blank=True, null=True)
    font_awesome_icon = models.CharField(max_length=128, blank=True, null=True)
    to_new_tab = models.BooleanField(default=True)

    def __str__(self):
        return self.page_name