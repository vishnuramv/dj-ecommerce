# Generated by Django 3.1.1 on 2020-09-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_order_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='being_delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='received',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='refund_granted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='refund_requested',
            field=models.BooleanField(default=False),
        ),
    ]
