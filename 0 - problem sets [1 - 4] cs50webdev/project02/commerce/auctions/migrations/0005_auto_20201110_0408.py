# Generated by Django 3.1.2 on 2020-11-10 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20201110_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='img_url',
            field=models.CharField(default='no_img', max_length=500),
        ),
    ]
