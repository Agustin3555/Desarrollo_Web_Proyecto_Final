# Generated by Django 3.1.7 on 2021-03-03 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuario_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cuenta', models.CharField(max_length=40, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('contrasenia', models.CharField(max_length=30)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=50)),
                ('descripcion_propia', models.CharField(max_length=500, null=True)),
                ('promedio_calificacion', models.DecimalField(decimal_places=2, max_digits=2, null=True)),
            ],
        ),
    ]
