# Generated by Django 4.2.2 on 2023-07-06 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('ID_servicio', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('Abogado', models.CharField(max_length=50, verbose_name='Abogado')),
                ('Tipo_de_Servicio', models.CharField(blank=True, max_length=90, null=True, verbose_name='Tipo_de_Servicio')),
                ('fecha_creacion', models.DateField(verbose_name='fecha_creacion')),
            ],
            options={
                'ordering': ['Abogado'],
            },
        ),
    ]
