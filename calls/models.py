from django.core.validators import RegexValidator
from django.db import models
import os
from __future__ import unicode_literals


class Contact(models.Model):

  ACTIVE = 'AC'
  INACTIVE = 'IN'
  STATUS_CHOICES = (
    ('ACTIVE', 'Ativo'),
    ('INACTIVE', 'Inativo'),
  )

  cellphone_regex = RegexValidator(regex=r'^\(\d{2}\)\d{1}\s\d{4}-\d{4}$', message="O número deve ser cadastrado da seguinte forma: (DD) 9 9999-9999")
  phone_regex = RegexValidator(regex=r'^\(\d{2}\)\d{4}-\d{4}$', message="O número deve ser cadastrado da seguinte forma: (DD) 9999-9999")
  email_regex = RegexValidator(regex=r'^([\w\-]+\.)*[\w\- ]+@([\w\- ]+\.)+([\w\-]{2,3})$', message="O email deve ser cadastrado da seguinte forma: email@email.com")

  name = models.CharField(max_length = 256, blank=False, verbose_name = "Nome")
  company_name = models.CharField(max_length = 40, blank=False, verbose_name = "Empresa")
  email = models.EmailField(max_length = 256, blank=False, validators = [email_regex], verbose_name = "Email do contato")
  cellphone = models.CharField(max_length = 11, validators = [cellphone_regex], verbose_name = "Celular")
  phone = models.CharField(max_length = 10, validators = [phone_regex], verbose_name = "Telefone")
  adress = models.CharField(max_length = 256, verbose_name = "Endereço")
  last_update = models.DateTimeField(auto_now = False, verbose_name = "Última atualização")
  status = models.CharField(max_length = 8, choices = STATUS_CHOICES, default = ACTIVE, verbose_name = "Status")
  tag = models.ForeignKey('Tag', on_delete = models.CASCADE, verbose_name = "Tag")

  class Meta:
        verbose_name_plural = "Contatos"
    def __str__(self):
        return self.name


class Tag(models.Model):
  name = models.Charfield(max_length = 50, primary_key = True, verbose_name = "Nome")

  class Meta:
        verbose_name_plural = "Tags"
    def __str__(self):
        return self.name

class Call(models.Model):

  call_id = models.AutoField(primary_key = True, verbose_name = "Número da Ligação")
  duration = models.TimeField(auto_now = False , verbose_name = "Duração")
  call_24_hours = models.BooleanField(default = False)
  email_sended = models.BooleanField(default = False)
  paid = models.BooleanField(default = False)
  notes = models.TextField(max_length = 256)
  subject = models.ForeignKey('Subject', on_delete = models.CASCADE, verbose_name = "Assunto")

  class Meta:
        verbose_name_plural = "Ligações"
    def __str__(self):
        return self.call_id

class Subject(models.Model):
  name = models.CharField(max_length = 256, primary_key = True, verbose_name = "Nome")

  class Meta:
        verbose_name_plural = "Assuntos"
    def __str__(self):
        return self.name


