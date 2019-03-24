# Generated by Django 2.1.5 on 2019-03-15 06:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0008_auto_20190222_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='subject',
            field=models.ManyToManyField(max_length=3, to='calls.Subject', verbose_name='Assunto'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='cellphone',
            field=models.CharField(help_text='O número deve ser cadastrado da seguinte forma:                      (DD)9-9999-9999', max_length=20, validators=[django.core.validators.RegexValidator(message='O número deve ser cadastrado da seguinte forma:                    (DD)9-9999-9999', regex='^\\(\\d{2}\\)\\d{1}-\\d{4}-\\d{4}$')], verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=256, validators=[django.core.validators.RegexValidator(message='O email deve ser cadastrado da seguinte forma:                     email@email.com', regex='^([\\w\\-]+\\.)*[\\w\\- ]+@([\\w\\- ]+\\.)+([\\w\\-]{2,3})$')], verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(help_text='O número deve ser cadastrado da seguinte forma:                    (DD)9999-9999', max_length=20, validators=[django.core.validators.RegexValidator(message='O número deve ser cadastrado da seguinte forma:                    (DD)9999-9999', regex='^\\(\\d{2}\\)\\d{4}-\\d{4}$')], verbose_name='Telefone'),
        ),
    ]