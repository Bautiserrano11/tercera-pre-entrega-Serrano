# Generated by Django 4.2.7 on 2023-11-28 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='fecha_publicacion',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='titulo',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='director',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='fecha_estreno',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='titulo',
        ),
    ]
