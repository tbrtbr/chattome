# Generated by Django 2.0 on 2021-11-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_product_descriptiontest'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stockcode',
            field=models.TextField(blank=True),
        ),
    ]