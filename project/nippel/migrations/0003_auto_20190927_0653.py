# Generated by Django 2.2.5 on 2019-09-27 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nippel', '0002_nippel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nippel',
            name='مدل',
            field=models.CharField(choices=[('darzdar', 'درزدار'), ('mannesmann', 'مانیسمان'), ('type40', 'رده چهل')], max_length=100),
        ),
    ]
