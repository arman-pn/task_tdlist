# Generated by Django 5.1.3 on 2024-12-07 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_alter_list_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='list',
            new_name='task',
        ),
    ]