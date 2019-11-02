from django.contrib import admin
from .models import Purchase
# Register your models here.

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'name' , 'model' , 'number' ,  'price')
    list_display_links = ('user' , 'name')
    search_fields = ('user' , )
admin.site.register(Purchase , PurchaseAdmin)