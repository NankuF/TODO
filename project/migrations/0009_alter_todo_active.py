# Generated by Django 3.2.8 on 2021-11-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_alter_todo_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
