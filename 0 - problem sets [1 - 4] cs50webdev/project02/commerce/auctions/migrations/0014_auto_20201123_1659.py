# Generated by Django 3.1.2 on 2020-11-23 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20201122_1824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='deleted',
            new_name='closed',
        ),
        migrations.AlterField(
            model_name='listing',
            name='time',
            field=models.CharField(default='2020-11-23 16:59:35', max_length=30),
        ),
    ]
