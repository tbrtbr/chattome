# Generated by Django 2.0 on 2021-11-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20211130_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='pricerule',
            field=models.IntegerField(default=0),
        ),
    ]