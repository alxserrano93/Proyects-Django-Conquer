# Generated by Django 5.1 on 2024-10-31 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_libro_out_of_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='editorial',
            name='level',
            field=models.CharField(choices=[('1', 'Nivel 1'), ('2', 'Nivel 2'), ('3', 'Nivel 3')], default='1', max_length=2),
        ),
    ]
