# Generated by Django 3.1.1 on 2020-09-18 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200918_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='inventory_value',
            new_name='current_stock',
        ),
    ]
