# Generated by Django 2.2.5 on 2019-11-01 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='تصویر',
            new_name='image',
        ),
    ]
