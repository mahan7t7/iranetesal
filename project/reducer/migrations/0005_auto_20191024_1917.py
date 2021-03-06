# Generated by Django 2.2.5 on 2019-10-24 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reducer', '0004_auto_20190927_0706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reducer',
            name='سایز_اول',
        ),
        migrations.RemoveField(
            model_name='reducer',
            name='سایز_دوم',
        ),
        migrations.AddField(
            model_name='reducer',
            name='سایز',
            field=models.CharField(choices=[('3/4"*1/2"', '3/4" * 1/2"'), ('1"*1/2"', '1" * 1/2"'), ('1"*3/4"', '1" * 3/4"'), ('1.1/4"*1"', '1.1/4" * 1"'), ('1.1/4"*3/4"', '1.1/4" * 3/4"'), ('1.1/4"*1/2"', '1.1/4" * 1/2"'), ('1.1/2"*1"', '1.1/2" * 1"'), ('1.1/2"*1.1/4"', '1.1/2" * 1.1/4"'), ('1.1/4"*1/2"', '1.1/4" * 1/2"'), ('1.1/2"*1/2"', '1.1/2" * 1/2"'), ('1.1/2"*3/4"', '1.1/2" * 3/4"'), ('2"*1.1/4"', '2" * 1.1/4"'), ('2"*1.1/2"', '2" * 1.1/2"'), ('2"*1"', '2" * 1"'), ('2"*1/2"', '2" * 1/2"'), ('2"*3/4"', '2" * 3/4"'), ('2.1/2"*1.1/2"', '2.1/2" * 1.1/2"'), ('2.1/2"*2"', '2.1/2" * 2"'), ('2.1/2"*1"', '2.1/2" * 1"'), ('2.1/2"*1.1/4"', '2.1/2" * 1.1/4"'), ('3"*1.1/2"', '3" * 1.1/2"'), ('3"*2"', '3" * 2"'), ('3"*2.1/2"', '3" * 2.1/2"'), ('3"*1"', '3" * 1"'), ('3"*1.1/4"', '3" * 1.1/4"'), ('4"*3"', '4" * 3"'), ('4"*2.1/2"', '4" * 2.1/2"'), ('4"*2"', '4" * 2"'), ('4"*1.1/4"', '4" * 1.1/4"'), ('4"*1.1/2"', '4" * 1.1/2"'), ('5"*3"', '5" * 3"'), ('5"*4"', '5" * 4"'), ('5"*21/2"', '5" * 21/2"'), ('6"*4"', '6" * 4"'), ('6"*5"', '6" * 5"'), ('6"*3"', '6" * 3"'), ('6"*21/2"', '6" * 21/2"'), ('8"*6"', '8" * 6"'), ('8"*5"', '8" * 5"'), ('8"*4"', '8" * 4"'), ('10"*8"', '10" * 8"'), ('10"*6"', '10" * 6"'), ('12"*10"', '12" * 10"'), ('12"*8"', '12" * 8"')], default='3/4"*1/2', max_length=100),
        ),
    ]
