from django.contrib import admin

from .models import Nippel
# Register your models here.

class NippelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'مدل', 'سایز', 'تعداد_کیسه', 'قیمت' )
    list_display_links = ('id' , 'name')
    list_filter = ('مدل', )
    list_editable = ('قیمت', )
    search_fields = ('مدل' , 'سایز')
    list_per_page = 25

admin.site.register(Nippel , NippelAdmin)