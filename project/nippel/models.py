from django.db import models
from pages.choices import NIPPEL_CHOICES
# Create your models here.

class Nippel(models.Model):
    NAME_CHOICES = [
        ('nippel', 'سردنده'),
    ]

    name = models.CharField(max_length=100 , choices=NAME_CHOICES , default='nippel')
    MODEL_CHOICES = [
        ('darzdar', 'درزدار'),
        ('mannesmann', 'مانیسمان'),
        ('type40', 'رده چهل'),
    ]
    مدل = models.CharField(max_length=100 , choices= MODEL_CHOICES)
    سایز = models.CharField(max_length=100, choices= NIPPEL_CHOICES)
    قیمت = models.IntegerField()

    NUMBER_CHOICES = [
        (800, 800),
        (600, 600),
        (400, 400),
        (300, 300),
        (200, 200),
        (100, 100),
        (60, 60),
        (40, 40),
        (20, 20),
        
        

    ]
    تعداد_کیسه = models.IntegerField(null=True , choices=NUMBER_CHOICES)

    def __str__(self):
        return self.name