from django.db import models

class Ac(models.Model):
    ac_io = models.BooleanField()
    ac_city = models.CharField(max_length=100)
    ac_temp = models.CharField(max_length=100)
