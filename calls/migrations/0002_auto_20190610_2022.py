# Generated by Django 2.1.5 on 2019-06-10 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='call',
            name='date',
        ),
        migrations.RemoveField(
            model_name='call',
            name='hour',
        ),
    ]