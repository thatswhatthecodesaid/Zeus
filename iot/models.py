from django.db import models
from main.models import *

class Ac(models.Model):
    ac_io = models.BooleanField()
    ac_city = models.CharField(max_length=100)
    ac_temp = models.CharField(max_length=100)


class Usage(models.Model):
    appliance = models.ForeignKey(Appliances, on_delete=models.CASCADE)
    start = models.TimeField(auto_now=False, auto_now_add=False)
    stop = models.TimeField(auto_now=False, auto_now_add=False)

