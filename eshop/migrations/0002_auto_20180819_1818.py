# Generated by Django 2.1 on 2018-08-19 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug', 'inventory_id')},
        ),
    ]
