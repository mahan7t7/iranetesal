# Generated by Django 2.2.5 on 2019-09-26 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nippel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('مدل', models.CharField(choices=[('Tee', 'درزدار'), ('Mannesmann', 'مانیسمان'), ('Type40', 'رده چهل')], max_length=100)),
                ('سایز', models.DecimalField(choices=[(2, '2 اینچ'), (2.5, '2.5 اینچ'), (3, '3 اینچ'), (4, '4 اینچ'), (5, '5 اینچ'), (6, '6 اینچ'), (7, '7 اینچ'), (8, '8 اینچ'), (10, '10 اینچ')], decimal_places=1, max_digits=2)),
                ('قیمت', models.IntegerField()),
                ('تعداد_کیسه', models.IntegerField(choices=[(800, 800), (600, 600), (400, 400), (300, 300), (200, 200), (100, 100), (60, 60), (40, 40), (20, 20)], null=True)),
            ],
        ),
    ]
