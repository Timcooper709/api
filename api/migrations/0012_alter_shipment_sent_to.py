# Generated by Django 4.1.5 on 2023-01-24 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_rename_shipping_shipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='sent_to',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
