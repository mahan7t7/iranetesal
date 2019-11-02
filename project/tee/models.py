from django.db import models
from pages.choices import TEE_CHOICES
# Create your models here.

class Tee(models.Model):
    NAME_CHOICES = [
        ('tee', 'سه راهی'),
    ]

    name = models.CharField(max_length=100 , choices=NAME_CHOICES , default='tee')
    MODEL_CHOICES = [
        ('darzdar', 'درزدار'),
        ('mannesmann', 'مانیسمان'),
        ('type40', 'رده چهل'),
    ]
    مدل = models.CharField(max_length=100 , choices= MODEL_CHOICES)
    سایز = models.CharField(max_length=100, choices=TEE_CHOICES , default='1/2"*X')
    قیمت = models.IntegerField()

    NUMBER_CHOICES = [
        (300, 300),
        (200, 200),
        (120, 120),
        (100, 100),
        (90, 90),
        (50, 50),
        (30, 30),
        (20, 20),
        (15, 15),
        
        

    ]
    تعداد_کیسه = models.IntegerField(null=True , choices=NUMBER_CHOICES)

    def __str__(self):
        return self.name