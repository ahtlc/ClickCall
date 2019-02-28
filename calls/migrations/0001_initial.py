# Generated by Django 2.1.7 on 2019-02-21 17:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('call_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Número da Ligação')),
                ('duration', models.TimeField(verbose_name='Duração')),
                ('call_24_hours', models.BooleanField(default=False)),
                ('email_sended', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('notes', models.TextField(max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Ligações',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Nome')),
                ('company_name', models.CharField(max_length=40, verbose_name='Empresa')),
                ('email', models.EmailField(max_length=256, validators=[django.core.validators.RegexValidator(message='O email deve ser cadastrado da seguinte forma: email@email.com', regex='^([\\w\\-]+\\.)*[\\w\\- ]+@([\\w\\- ]+\\.)+([\\w\\-]{2,3})$')], verbose_name='Email do contato')),
                ('cellphone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='O número deve ser cadastrado da seguinte forma: (DD) 9 9999-9999', regex='^\\(\\d{2}\\)\\d{1}\\s\\d{4}-\\d{4}$')], verbose_name='Celular')),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='O número deve ser cadastrado da seguinte forma: (DD) 9999-9999', regex='^\\(\\d{2}\\)\\d{4}-\\d{4}$')], verbose_name='Telefone')),
                ('adress', models.CharField(max_length=256, verbose_name='Endereço')),
                ('last_update', models.DateTimeField(verbose_name='Última atualização')),
                ('status', models.CharField(choices=[('ACTIVE', 'Ativo'), ('INACTIVE', 'Inativo')], default='AC', max_length=8, verbose_name='Status')),
            ],
            options={
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('name', models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='Nome')),
            ],
            options={
                'verbose_name_plural': 'Assuntos',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Nome')),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calls.Tag', verbose_name='Tag'),
        ),
        migrations.AddField(
            model_name='call',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calls.Subject', verbose_name='Assunto'),
        ),
    ]