# Generated by Django 2.1.5 on 2019-04-04 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0002_call_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='status',
            field=models.CharField(choices=[('RECEBIDA', 'Recebida'), ('ATENDIDA', 'Atendida'), ('NAO_ATENDIDA', 'Não Atendida'), ('ABANDONADA', 'Abandonada')], default='RC', max_length=12, verbose_name='Status'),
        ),
    ]
