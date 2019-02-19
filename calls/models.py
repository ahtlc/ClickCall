from django.core.validators import RegexValidator
from django.db import models
import os
from __future__ import unicode_literals


class Contact(models.Model):
    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    name = models.CharField(max_length = 80, blank=False)
    company_name = models.CharField(max_length = 40, blank=False)
    email = models.EmailField(max_length = 256, blank=False)
    cellphone = models.CharField(max_length = 11)
    phone = models.CharField(max_length = 10, validators = [phone_regex])
    adress = models.CharField(max_length = 256)
    tag = models.ForeignKey('Tag', on_delete = models.CASCADE)


class Tag(models.Model):

