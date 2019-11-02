from django.db import models
from pages.choices import REDUCER_CHOICES
# Create your models here.

class Reducer(models.Model):
    NAME_CHOICES = [
        ('reducer', 'تبدیل'),
    ]

    name = models.CharField(max_length=100 , choices=NAME_CHOICES , default='reducer')
    MODEL_CHOICES = [
        ('darzdar', 'درزدار'),
        ('mannesmann', 'مانیسمان'),
        ('type40', 'رده چهل'),
    ]
    مدل = models.CharField(max_length=100 , choices= MODEL_CHOICES)
    
    سایز = models.CharField(max_length=100 , choices =REDUCER_CHOICES , default='3/4"*1/2')

    قیمت = models.IntegerField()

    NUMBER_CHOICES = [
        (400, 400),
        (300, 300),
        (200, 200),
        (120, 120),
        (80, 80),
        (50, 50),
        (30, 30),
        (20, 20),
        (15, 15),

    ]
    تعداد_کیسه = models.IntegerField(null=True , choices=NUMBER_CHOICES)

    def __str__(self):
        return self.name