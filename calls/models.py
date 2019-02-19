from django.db import models
import os
from __future__ import unicode_literals


class Contact(models.Model):
    name = models.CharField(max_length = 80, blank=False)
    company_name = models.CharField(max_length = 40, blank=False)
    email = models.EmailField(max_length = 256, blank=False)
    cellphone = models.CharField(max_length = 11)
    phone = models.CharField(max_length = 10)
    adress = models.CharField(max_length = 256)
    tag = models.ForeignKey('Tag', on_delete = models.CASCADE)
# Create your models here.

class Tag(models.Model):

