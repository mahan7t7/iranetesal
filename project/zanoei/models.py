from django.db import models
from pages.choices import ELBOW_CHOICES
# Create your models here.

class Elbow(models.Model):
    NAME_CHOICES = [
        ('elbow', 'زانویی'),
    ]

    name = models.CharField(max_length=100 , choices=NAME_CHOICES , default='elbow')
    MODEL_CHOICES = [
        ('darzdar', 'درزدار '),
        ('standard', 'استاندارد'),
        ('mannesmann', 'مانیسمان'),
        ('type40', 'رده چهل'),
    ]
    مدل = models.CharField(max_length=100 , choices= MODEL_CHOICES)
    سایز = models.CharField(max_length=100, choices= ELBOW_CHOICES)
    قیمت = models.IntegerField()
    NUMBER_CHOICES = [
        (350, 350),
        (250, 250),
        (170, 170),
        (130, 130),
        (110, 110),
        (55, 55),
        (30, 30),
        (25, 25),
        (15, 15),
        (8, 8),
        (5, 5),
        

    ]
    تعداد_کیسه = models.IntegerField(null=True , choices=NUMBER_CHOICES)

    def __str__(self):
        return self.name
    