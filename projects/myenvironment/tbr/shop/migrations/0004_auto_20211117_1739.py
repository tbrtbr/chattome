# Generated by Django 2.0 on 2021-11-17 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20211117_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='customerfeedback',
            new_name='customer_Feedback',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='logisticcost',
            new_name='logistic_Cost',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='logisticvendor',
            new_name='logistic_Vendor',
        ),
        migrations.AddField(
            model_name='category',
            name='Cat_ID',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='category',
            name='published_At',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='category',
            name='pulbished_Only_Web',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='remarks',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='remarks',
            field=models.TextField(blank=True),
        ),
    ]