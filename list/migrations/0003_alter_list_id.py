# Generated by Django 5.1.1 on 2024-12-03 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_category_list_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
