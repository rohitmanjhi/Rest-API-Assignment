# Generated by Django 3.1.1 on 2020-09-18 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inventory',
            unique_together={('product', 'color', 'size')},
        ),
    ]
