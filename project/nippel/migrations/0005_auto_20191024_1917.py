# Generated by Django 2.2.5 on 2019-10-24 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nippel', '0004_auto_20190927_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nippel',
            name='سایز',
            field=models.CharField(choices=[('1/2"', '1/2"'), ('3/4"', '3/4"'), ('1"', '1"'), ('1.1/4"', '1.1/4"'), ('1.1/2"', '1.1/2"'), ('2"', '2"'), ('2.1/2"', '2.1/2"'), ('3"', '3"'), ('4"', '4"')], max_length=100),
        ),
    ]
