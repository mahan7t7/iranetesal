# Generated by Django 2.2.5 on 2019-09-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reducer', '0003_auto_20190927_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reducer',
            name='سایز_اول',
            field=models.DecimalField(choices=[(2, '2 اینچ'), (2.5, '2.5 اینچ'), (3, '3 اینچ'), (4, '4 اینچ'), (5, '5 اینچ'), (6, '6 اینچ'), (7, '7 اینچ'), (8, '8 اینچ'), (10, '10 اینچ')], decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='reducer',
            name='سایز_دوم',
            field=models.DecimalField(choices=[(2, '2 اینچ'), (2.5, '2.5 اینچ'), (3, '3 اینچ'), (4, '4 اینچ'), (5, '5 اینچ'), (6, '6 اینچ'), (7, '7 اینچ'), (8, '8 اینچ'), (10, '10 اینچ')], decimal_places=1, max_digits=3),
        ),
    ]
