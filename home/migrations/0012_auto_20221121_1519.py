# Generated by Django 3.2 on 2022-11-21 09:49

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20221120_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='todo',
            name='Due_Date',
            field=models.DateField(blank=True, default=None, null=True, validators=[home.models.validate_date]),
        ),
        migrations.AlterField(
            model_name='todo',
            name='Title',
            field=models.CharField(max_length=100),
        ),
    ]
