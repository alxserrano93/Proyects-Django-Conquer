# Generated by Django 5.1 on 2024-09-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_editorial_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorial',
            name='sitio_web',
            field=models.URLField(blank=True, null=True),
        ),
    ]
