# Generated by Django 4.1.5 on 2023-01-24 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_shipment_sent_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='address_line_one',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shipment',
            name='address_line_two',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
