# Generated by Django 3.1.7 on 2021-03-05 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0003_auto_20210305_1656'),
        ('mascota', '0004_auto_20210305_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='publicacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publicacion.publicacion'),
        ),
    ]
