# Generated by Django 3.0.2 on 2020-05-24 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis_productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto_fotos',
            old_name='foto1',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='producto_fotos',
            name='foto2',
        ),
        migrations.RemoveField(
            model_name='producto_fotos',
            name='foto3',
        ),
        migrations.RemoveField(
            model_name='producto_fotos',
            name='foto4',
        ),
        migrations.AlterField(
            model_name='producto_precios',
            name='productos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lista_precios', to='apis_productos.Productos'),
        ),
    ]
