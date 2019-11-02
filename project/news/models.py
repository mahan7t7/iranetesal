from django.db import models
from datetime import datetime
# Create your models here.

class News(models.Model):
    عنوان = models.CharField(max_length=255)
    توضیحات = models.TextField()
    image = models.ImageField(upload_to='photos', blank=True)
    تاریخ_انتشار = models.DateTimeField (default=datetime.now)

    def __str__(self):
        return self.عنوان