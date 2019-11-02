from django.contrib import admin
from .models import Sold
class SoldAdmin(admin.ModelAdmin):
    list_display = ('user','کد_پیگیری' ,'name', 'model', 'size', 'number', 'price', 'بررسی_شده', 'ارسال_شده', 'تاریخ_خرید', 'پرداخت_چکی')
    list_display_links = ('user' , 'کد_پیگیری')
    list_filter = ('بررسی_شده', 'ارسال_شده', 'تاریخ_خرید', 'پرداخت_چکی' )
    list_editable = ('ارسال_شده', 'پرداخت_چکی')
    search_fields = ('بررسی_شده', 'ارسال_شده', 'تاریخ_خرید', 'پرداخت_چکی')
    list_per_page = 25

admin.site.register(Sold , SoldAdmin)