# Generated by Django 5.1 on 2024-08-07 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_created_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='Courses',
        ),
    ]