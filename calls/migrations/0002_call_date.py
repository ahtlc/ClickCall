# Generated by Django 2.1.7 on 2019-03-12 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Data da Ligação'),
        ),
    ]
