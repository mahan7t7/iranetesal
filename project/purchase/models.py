from django.db import models
from accounts.models import User
from django.core.mail import EmailMessage

# Create your models here.

class PurchaseManager (models.Manager):
    def create_purchase (self, user , name , model , size , number , price , purchased):
        purchase = self.create(user=user , name=name , model=model , size=size , number=number , price=price , purchased=purchased)
        purchase.save()
        return purchase


class Purchase (models.Model):
    
    user = models.ForeignKey (User , on_delete=models.CASCADE,primary_key=False)
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    size = models. CharField(max_length=100, null=True)
    number = models.CharField(max_length=100)
    price = models.IntegerField ()
    purchased = models.BooleanField(default=False)

    objects = PurchaseManager()

    