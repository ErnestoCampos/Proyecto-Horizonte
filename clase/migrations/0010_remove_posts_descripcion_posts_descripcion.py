# Generated by Django 4.0.3 on 2022-04-30 22:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0009_alter_posts_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='Descripcion',
        ),
        migrations.AddField(
            model_name='posts',
            name='descripcion',
            field=ckeditor.fields.RichTextField(default='Escribe Aqui', max_length=340),
        ),
    ]
