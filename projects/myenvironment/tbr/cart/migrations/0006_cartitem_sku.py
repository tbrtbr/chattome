# Generated by Django 2.0 on 2021-11-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20211130_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='SKU',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
