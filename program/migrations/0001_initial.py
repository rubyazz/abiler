# Generated by Django 4.1.2 on 2022-10-11 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.IntegerField(max_length=200)),
                ('instagram', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Abi',
                'verbose_name_plural': 'Abies',
            },
        ),
    ]
