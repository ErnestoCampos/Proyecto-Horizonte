# Generated by Django 4.0.3 on 2022-03-18 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0002_alter_curso_camada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Autor', models.CharField(max_length=30)),
                ('FechaDePublicacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Autor', models.CharField(max_length=30)),
                ('FechaDePublicacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=40)),
                ('contraseña', models.CharField(max_length=25)),
                ('registrado', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]