# Generated by Django 4.1.2 on 2022-10-18 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0004_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cabCompus',
        ),
        migrations.DeleteModel(
            name='cabDormitory',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.RemoveField(
            model_name='event',
            name='place',
        ),
    ]