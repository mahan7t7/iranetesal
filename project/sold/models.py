from django.db import models
from datetime import datetime
from accounts.models import User
import random
import string
# Create your models here.
class SoldManager(models.Manager):
    def validate_sold(self , user , name , model , size , number , price):
        sold_id = create_unique_id()
        unique = False
        while not unique:
            try:
                check = Sold.objects.get(کد_پیگیری=sold_id)
                if check:
                    sold_id = create_unique_id()
                else:
                    unique=True   
            except:
                unique=True
        sold = self.create(user=user, name=name, model=model, size=size, number=number, price=price , کد_پیگیری=sold_id)
        sold.save()
        return sold

def create_unique_id():
    return ''.join(random.choices(string.digits, k=8))


class Sold(models.Model):
    user = models.ForeignKey (User , on_delete=models.DO_NOTHING, primary_key=False)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    بررسی_شده = models.BooleanField(default=False)
    ارسال_شده = models.BooleanField(default=False)
    پرداخت_چکی = models.BooleanField(default=False)
    تاریخ_خرید = models.DateTimeField(auto_now=True)
    کد_پیگیری = models.CharField(max_length=8 , unique=True , primary_key=True)

    objects = SoldManager()
