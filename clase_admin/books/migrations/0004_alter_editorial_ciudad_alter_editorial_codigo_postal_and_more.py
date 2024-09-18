# Generated by Django 5.1 on 2024-09-05 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_autores_autor_libro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorial',
            name='ciudad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='codigo_postal',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='direccion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='estado',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='pais',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]