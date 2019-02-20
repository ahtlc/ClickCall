from django.core.validators import RegexValidator
from django.db import models
import os
from __future__ import unicode_literals


class Contact(models.Model):

  name = models.CharField(max_length = 80, blank=False)
  company_name = models.CharField(max_length = 40, blank=False)
  email = models.EmailField(max_length = 256, blank=False, validators = [email_regex])
  cellphone = models.CharField(max_length = 11, validators = [cellphone_regex])
  phone = models.CharField(max_length = 10, validators = [phone_regex])
  adress = models.CharField(max_length = 256)
  tag = models.ForeignKey('Tag', on_delete = models.CASCADE)

  cellphone_regex = RegexValidator(regex=r'^\(\d{2}\)\d{1}\s\d{4}-\d{4}$', message="O número deve ser cadastrado da seguinte forma: (DD) 9 9999-9999")
  phone_regex = RegexValidator(regex=r'^\(\d{2}\)\d{4}-\d{4}$', message="O número deve ser cadastrado da seguinte forma: (DD) 9999-9999")
  email_regex = RegexValidator(regex=r'^([\w\-]+\.)*[\w\- ]+@([\w\- ]+\.)+([\w\-]{2,3})$', message="O email deve ser cadastrado da seguinte forma: email@email.com")


class Tag(models.Model):
  name = models.Charfield(max_length = 50)


