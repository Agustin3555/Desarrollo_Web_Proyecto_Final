# Generated by Django 3.1.7 on 2021-03-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0010_mascota_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='edad',
            field=models.PositiveIntegerField(),
        ),
    ]
