# Generated by Django 2.0 on 2021-11-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='stockcode',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='product',
            name='stockcode',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]