# Generated by Django 2.0 on 2021-11-17 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20211116_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='customerfeedback',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='logisticcost',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='product',
            name='logisticvendor',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
