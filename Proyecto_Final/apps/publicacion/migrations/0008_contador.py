# Generated by Django 3.1.7 on 2021-03-09 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0007_auto_20210307_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contador',
            fields=[
                ('id_contador', models.AutoField(primary_key=True, serialize=False)),
                ('i', models.PositiveIntegerField()),
                ('Publicacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='publicacion.publicacion')),
            ],
        ),
    ]
