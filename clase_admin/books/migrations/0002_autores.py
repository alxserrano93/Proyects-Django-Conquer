# Generated by Django 5.0.7 on 2024-08-03 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=100)),
                ('biografia', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('sitio_web', models.URLField()),
                ('premios', models.TextField()),
            ],
        ),
    ]
