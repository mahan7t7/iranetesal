# Generated by Django 2.2.5 on 2019-11-01 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20191101_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
    ]
