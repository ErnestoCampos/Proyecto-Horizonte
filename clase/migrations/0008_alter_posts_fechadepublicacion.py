# Generated by Django 4.0.3 on 2022-04-15 20:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0007_alter_posts_fechadepublicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='FechaDePublicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
