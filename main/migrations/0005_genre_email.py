# Generated by Django 3.0.2 on 2020-01-18 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]