# Generated by Django 3.1.7 on 2021-02-27 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_Denuncia',
            fields=[
                ('id_datos_denuncia', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('tipo', models.CharField(max_length=1)),
                ('comentario', models.CharField(max_length=500)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Denuncias',
            fields=[
                ('id_denuncias', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('usuario_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('contrasenia', models.CharField(max_length=30)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=50)),
                ('descripcion_propia', models.CharField(max_length=500, null=True)),
                ('promedio_calificacion', models.DecimalField(decimal_places=2, max_digits=2, null=True)),
                ('denuncias', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='post.denuncias')),
            ],
        ),
        migrations.CreateModel(
            name='Nodo_Denuncia',
            fields=[
                ('id_nodo_denuncia', models.AutoField(primary_key=True, serialize=False)),
                ('datos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='post.datos_denuncia')),
                ('nodo_anterior', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='post.nodo_denuncia')),
                ('nodo_siguiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='post.nodo_denuncia')),
            ],
        ),
        migrations.AddField(
            model_name='denuncias',
            name='primer_nodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='post.nodo_denuncia'),
        ),
        migrations.AddField(
            model_name='denuncias',
            name='ultimo_nodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='post.nodo_denuncia'),
        ),
        migrations.AddField(
            model_name='datos_denuncia',
            name='usuario_denunciado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='post.usuarios'),
        ),
    ]
