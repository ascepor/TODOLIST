# Generated by Django 3.2 on 2022-11-20 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20221120_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='Decription',
            new_name='Description',
        ),
    ]