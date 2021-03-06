# Generated by Django 4.0.3 on 2022-04-03 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0005_remove_comentario_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='Descripcion',
            field=models.TextField(default='Escribe Aqui', max_length=340),
        ),
        migrations.AddField(
            model_name='posts',
            name='Imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='FechaDePublicacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
