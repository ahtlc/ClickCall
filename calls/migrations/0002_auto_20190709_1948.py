# Generated by Django 2.1.5 on 2019-07-09 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor'),
        ),
    ]
