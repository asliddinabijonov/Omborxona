from django.contrib import admin
from .models import *

@admin.register(Tarqatuvchi)
class LoginViewsAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')