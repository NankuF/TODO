# Generated by Django 3.2.8 on 2021-11-08 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_alter_todo_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]