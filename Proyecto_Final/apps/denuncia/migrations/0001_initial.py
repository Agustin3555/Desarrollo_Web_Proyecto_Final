# Generated by Django 3.1.7 on 2021-03-04 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id_denuncia', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('tipo', models.CharField(max_length=1)),
                ('comentario', models.CharField(max_length=500)),
                ('estado', models.BooleanField(null=True)),
            ],
        ),
    ]
