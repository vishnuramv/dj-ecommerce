# Generated by Django 3.1.1 on 2020-09-03 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_order_billing_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
