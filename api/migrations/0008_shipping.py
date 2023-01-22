# Generated by Django 4.1.5 on 2023-01-22 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_item_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_to', models.TextField(blank=True, null=True)),
                ('quantity_shipped', models.IntegerField(blank=True, null=True)),
                ('tracking_number', models.CharField(blank=True, max_length=50, null=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to='api.item')),
            ],
        ),
    ]