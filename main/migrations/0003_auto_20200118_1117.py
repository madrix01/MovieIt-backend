# Generated by Django 3.0.2 on 2020-01-18 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_genre_drama'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='children',
            new_name='family',
        ),
    ]