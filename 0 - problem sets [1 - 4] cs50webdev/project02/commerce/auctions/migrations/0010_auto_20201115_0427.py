# Generated by Django 3.1.2 on 2020-11-15 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20201113_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bid',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=14),
        ),
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='bid',
            name='listing_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='listing_bids', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='owner',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='listing',
            name='time',
            field=models.CharField(default='2020-11-15 04:27:39', max_length=30),
        ),
    ]
