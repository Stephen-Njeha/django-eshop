# Generated by Django 2.1 on 2018-09-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180905_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
