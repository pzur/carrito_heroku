# Generated by Django 3.0.2 on 2020-05-28 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis_productos', '0003_auto_20200527_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto_fotos',
            old_name='photo1',
            new_name='photo_1',
        ),
        migrations.RenameField(
            model_name='producto_fotos',
            old_name='photo2',
            new_name='photo_2',
        ),
        migrations.RenameField(
            model_name='producto_fotos',
            old_name='photo3',
            new_name='photo_3',
        ),
        migrations.RenameField(
            model_name='producto_fotos',
            old_name='photo4',
            new_name='photo_4',
        ),
    ]
