# Generated by Django 3.2 on 2022-11-20 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_created_on_todo_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='Status',
            field=models.CharField(choices=[('open', 'OPEN'), ('working', 'WORKING'), ('done', 'DONE'), ('overdue', 'OVERDUE')], default='OPEN', max_length=7),
        ),
    ]
