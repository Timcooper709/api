# Generated by Django 4.1.5 on 2023-01-24 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_shipment_address_line_one_shipment_address_line_two'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipment',
            old_name='sent_to',
            new_name='attn',
        ),
    ]
