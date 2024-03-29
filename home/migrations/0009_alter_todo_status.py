# Generated by Django 3.2 on 2022-11-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Status',
            field=models.CharField(choices=[('open', 'OPEN'), ('working', 'WORKING'), ('done', 'DONE'), ('overdue', 'OVERDUE')], default='OPEN', max_length=7, unique=True),
        ),
    ]
