# Generated by Django 2.0 on 2021-11-08 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_descriptiontest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='descriptiontest',
        ),
    ]
