# Generated by Django 2.0 on 2021-11-09 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20211108_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='descriptiontest',
        ),
    ]
