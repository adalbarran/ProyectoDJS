# Generated by Django 4.2.2 on 2023-07-08 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CasoAbogados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abogado',
            fields=[
                ('rut', models.AutoField(db_column='rut', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True, verbose_name='nombre ')),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(max_length=20)),
                ('fec_nac', models.DateField()),
                ('telefono', models.CharField(max_length=9)),
                ('area', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='img')),
            ],
            options={
                'ordering': ['rut'],
            },
        ),
    ]