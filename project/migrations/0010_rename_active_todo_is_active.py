# Generated by Django 3.2.8 on 2021-11-03 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_todo_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='active',
            new_name='is_active',
        ),
    ]
