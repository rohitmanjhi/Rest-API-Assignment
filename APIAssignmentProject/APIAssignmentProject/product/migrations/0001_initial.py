# Generated by Django 3.1.1 on 2020-09-18 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('inventory_value', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.size')),
            ],
            options={
                'unique_together': {('product', 'size'), ('product', 'color')},
            },
        ),
    ]