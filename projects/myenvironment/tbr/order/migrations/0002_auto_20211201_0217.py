# Generated by Django 2.0 on 2021-11-30 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('token',), 'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='billingAddress1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='billingCity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='billingCountry',
        ),
        migrations.RemoveField(
            model_name='order',
            name='billingName',
        ),
        migrations.RemoveField(
            model_name='order',
            name='billingPostcode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shippingAddress1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shippingCity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shippingCountry',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shippingName',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shippingPostcode',
        ),
        migrations.AlterModelTable(
            name='order',
            table=None,
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
