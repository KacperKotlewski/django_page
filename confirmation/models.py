from django.db import models
from order_form.models import Orders

import random
import string

# Create your models here.

class Confirmations_link(models.Model):
    link = models.CharField(max_length=32, unique=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, blank=True, null=True)

    def NewLink(from_order):
        random.seed(from_order.id)
        newlink = generate_link()
        while(Confirmations_link.objects.filter(link=newlink).count() != 0):
            newlink = generate_link()

        conf = Confirmations_link.objects.create(link=newlink, order=from_order)
        conf.save()
        

        return ("/confirmation/" + newlink)

def generate_link():
    newlink = ""
    for i in range(16):
        if(random.randint(0,100)%3 == 0):
            newlink += str(random.randint(0,9))
        else:
            newlink += random.choice(string.ascii_letters)

    return newlink