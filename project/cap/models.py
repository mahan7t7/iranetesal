from django.db import models
from pages.choices import CAP_CHOICES
# Create your models here.

class Cap(models.Model):
    NAME_CHOICES = [
        ('cap', 'کپ'),
    ]

    name = models.CharField(max_length=100 , choices=NAME_CHOICES , default='cap')
    
    MODEL_CHOICES = [
        ('deep', 'گود'),
        ('flat', 'تخت'),
    ]
    مدل = models.CharField(max_length=100 , choices= MODEL_CHOICES)
    سایز = models.CharField(max_length=100 , choices= CAP_CHOICES)
    قیمت = models.IntegerField()
    NUMBER_CHOICES = [
        (3000, 3000),
        (2000, 2000),
        (1000, 1000),
        (500, 500),
        (300, 300),
        (250, 250),
        (200, 200),
        (100, 100),
        (75, 75),
        (50, 50),
    ]
    تعداد_کیسه = models.IntegerField(null=True , choices=NUMBER_CHOICES)

    def __str__(self):
        return self.name