# Generated by Django 4.1.7 on 2024-01-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_rename_kitchen_resturant_items_kitchen_nam'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp_billing',
            name='bill_no',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
