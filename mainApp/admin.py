from django.contrib import admin
from .models import *

@admin.register(Mijoz)
class MijozAdmin(admin.ModelAdmin):
    list_display = ('ism', )

@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    list_display = ('nom', )
