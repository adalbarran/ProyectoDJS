# Generated by Django 4.2.2 on 2023-07-08 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CasoAbogados', '0003_caso'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicios',
            options={'ordering': ['ID_servicio']},
        ),
    ]