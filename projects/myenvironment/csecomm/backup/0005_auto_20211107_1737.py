# Generated by Django 2.0 on 2021-11-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20211107_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stockcode',
            field=models.TextField(blank=True),
        ),
    ]