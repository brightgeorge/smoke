# Generated by Django 4.1.7 on 2024-01-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0014_kitchen_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp_billing',
            name='billed_by',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
