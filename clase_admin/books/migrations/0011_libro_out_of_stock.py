# Generated by Django 5.1 on 2024-10-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_libro_autores'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='out_of_stock',
            field=models.BooleanField(default=False, verbose_name='Fuera de Stock'),
        ),
    ]