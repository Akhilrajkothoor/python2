# Generated by Django 4.0.4 on 2022-05-23 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_headss'),
    ]

    operations = [
        migrations.RenameField(
            model_name='headss',
            old_name='desc',
            new_name='descs',
        ),
        migrations.RenameField(
            model_name='headss',
            old_name='img',
            new_name='imgs',
        ),
        migrations.RenameField(
            model_name='headss',
            old_name='name',
            new_name='names',
        ),
    ]
